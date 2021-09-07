/* autor: JoseArevalo, date: 05/07/2021 */

/* 1)  ¿Qué consulta ejecutaría para obtener los ingresos totales para marzo de 2012? */
SELECT MONTHNAME(charged_datetime) AS month, SUM(billing.amount) AS revenue 
FROM billing
WHERE charged_datetime >= '2012-02-29 00:00:00' AND charged_datetime <= '2012-03-31 00:00:00';

/* 2)  ¿Qué consulta ejecutaría para obtener los ingresos totales recaudados del cliente con una identificación de 2? */
SELECT client_id, SUM(billing.amount) AS revenue 
FROM billing
WHERE client_id = 2;

/* 3)  ¿Qué consulta ejecutaría para obtener todos los sitios que posee client = 10? */
SELECT domain_name AS website, client_id
FROM sites
WHERE client_id = 10;

/* 4) ¿Qué consulta ejecutaría para obtener el número total de sitios creados por mes por año 
para el cliente con una identificación de 1? ¿Qué pasa con el cliente = 20? */
SELECT client_id, COUNT(client_id) AS number_of_websites,
MONTHNAME(created_datetime) AS month_created, YEAR(created_datetime) as Year
FROM sites
WHERE client_id = 1 OR client_id = 20
GROUP BY created_datetime ORDER BY client_id;

/* 5) ¿Qué consulta ejecutaría para obtener el número total de clientes potenciales generados 
para cada uno de los sitios entre el 1 de enero de 2011 y el 15 de febrero de 2011?*/
SELECT sites.domain_name AS website, COUNT(leads_id) AS number_of_leads, 
DATE_FORMAT(leads.registered_datetime, "%M %d, %Y") AS date_generated
FROM sites
LEFT JOIN leads ON leads.leads_id = sites.site_id
WHERE registered_datetime >= '2010-12-31 00:00:00' AND registered_datetime <= '2011-02-15 00:00:00'
GROUP BY registered_datetime;

/* 6) ¿Qué consulta ejecutaría para obtener una lista de nombres de clientes y el número total 
de clientes potenciales que hemos generado para cada uno de nuestros clientes entre el 
1 de enero de 2011 y el 31 de diciembre de 2011?  */
SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, 
COUNT(leads_id) AS number_of_leads
FROM clients
JOIN sites ON sites.client_id = clients.client_id
JOIN leads ON leads.site_id = sites.site_id
WHERE registered_datetime >= '2010-12-31 00:00:00' AND registered_datetime <= '2011-12-31 00:00:00'
GROUP BY clients.client_id;

/* 7) ¿Qué consulta ejecutaría para obtener una lista de nombres de clientes y el número total 
de clientes potenciales que hemos generado para cada cliente cada mes entre los meses 1 y 6 del año 2011? */
SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, 
COUNT(leads_id) AS number_of_leads, MONTHNAME(registered_datetime) AS month_generated
FROM clients
JOIN sites ON sites.client_id = clients.client_id
JOIN leads ON leads.site_id = sites.site_id
WHERE registered_datetime >= '2010-12-31 00:00:00' AND registered_datetime <= '2011-06-30 00:00:00'
GROUP BY leads.leads_id; 

/* 8) ¿Qué consulta ejecutaría para obtener una lista de nombres de clientes y el número total de clientes 
potenciales que hemos generado para cada uno de los sitios de nuestros clientes entre el 1 de enero de 2011 
y el 31 de diciembre de 2011? Solicite esta consulta por ID de cliente. Presente una segunda consulta que muestre 
todos los clientes, los nombres del sitio y el número total de clientes potenciales generados en cada sitio en todo momento. */
SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, 
sites.domain_name AS website, COUNT(leads_id) AS number_of_leads, 
DATE_FORMAT(registered_datetime, "%M %d, %Y") AS date_generated
FROM clients
JOIN sites ON sites.client_id = clients.client_id
JOIN leads ON leads.site_id = sites.site_id
WHERE registered_datetime >= '2010-12-31 00:00:00' AND registered_datetime <= '2011-12-31 00:00:00'
GROUP BY sites.site_id; 

SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, 
sites.domain_name AS website, COUNT(leads_id) AS number_of_leads
FROM clients
JOIN sites ON sites.client_id = clients.client_id
JOIN leads ON leads.site_id = sites.site_id
GROUP BY sites.site_id ORDER BY clients.client_id; 

/* 9) Escriba una sola consulta que recupere los ingresos totales recaudados de cada 
cliente para cada mes del año. Pídalo por ID de cliente. */
SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, 
SUM(billing.amount) AS Total_Revenue, MONTHNAME(billing.charged_datetime) AS month_change,
YEAR(billing.charged_datetime) AS year_charge
FROM clients
JOIN billing ON clients.client_id = billing.client_id
GROUP BY billing.charged_datetime
ORDER BY clients.client_id;

/* 10) Escriba una sola consulta que recupere todos los sitios que posee cada cliente. 
Agrupe los resultados para que cada fila muestre un nuevo cliente. 
Se volverá más claro cuando agregue un nuevo campo llamado 'sitios' que tiene todos los 
sitios que posee el cliente. (SUGERENCIA: use GROUP_CONCAT)  */
SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, 
GROUP_CONCAT(DISTINCT sites.domain_name SEPARATOR ' / ' ) AS sites
FROM clients
JOIN sites ON clients.client_id = sites.client_id
GROUP BY clients.client_id;








