/* autor: JoseArevalo, date: 05/07/2021 */

SELECT users.first_name, users.last_name, 
user2.first_name as friend_first_name, user2.last_name as friend_last_name
FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON friendships.friend_id = user2.id;

/* 1) Devuelva a todos los usuarios que son amigos de Kermit, 
asegúrese de que sus nombres se muestren en los resultados. */
SELECT users.first_name, users.last_name, 
user2.first_name as friend_first_name, user2.last_name as friend_last_name
FROM users LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON friendships.friend_id = user2.id
WHERE friendships.friend_id = 4;

/* 2) Devuelve el recuento de todas las amistades. */
SELECT COUNT(friendships.id) as total_friendships
FROM friendships;

 /* 3) Descubre quién tiene más amigos y devuelve el recuento de sus amigos. */ 
 SELECT CONCAT_WS(" ", users.first_name, users.last_name) as names,
 COUNT(friendships.user_id) AS total_friends 
 FROM friendships 
 LEFT JOIN users ON users.id = friendships.user_id
 GROUP BY friendships.user_id;

 /* 4) Crea un nuevo usuario y hazlos amigos de Eli Byers, Kermit The Frog y Marky Mark. */
SELECT * FROM users;
INSERT INTO `amigos`.`users` (`id`, `first_name`, `last_name`) VALUES ('6', 'Mario ', 'Bros');
SELECT * FROM friendships;
INSERT INTO `amigos`.`friendships` (`id`, `user_id`, `friend_id`) VALUES ('7', '2', '6');
INSERT INTO `amigos`.`friendships` (`id`, `user_id`, `friend_id`) VALUES ('8', '4', '6');
INSERT INTO `amigos`.`friendships` (`id`, `user_id`, `friend_id`) VALUES ('9', '5', '6');
SELECT users.first_name, users.last_name, 
user2.first_name as friend_first_name, user2.last_name as friend_last_name
FROM users LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON friendships.friend_id = user2.id
WHERE friendships.friend_id = 6;

 /*5) Devuelve a los amigos de Eli en orden alfabético. */
SELECT users.first_name, users.last_name, 
user2.first_name as friend_first_name, user2.last_name as friend_last_name
FROM users LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON friendships.friend_id = user2.id
WHERE friendships.user_id = 2
ORDER BY user2.first_name;

/* 6) Elimina a Marky Mark de los amigos de Eli */
SELECT * FROM friendships;
DELETE FROM `amigos`.`friendships` WHERE (`id` = '5');
SELECT users.first_name, users.last_name, 
user2.first_name as friend_first_name, user2.last_name as friend_last_name
FROM users LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON friendships.friend_id = user2.id
WHERE friendships.user_id = 2
ORDER BY user2.first_name;

/*6) Devuelve todas las amistades, mostrando solo el nombre y apellido de ambos amigos*/
SELECT CONCAT_WS(" ", users.first_name, users.last_name) as name, 
CONCAT_WS(" ", user2.first_name, user2.last_name) as friend
FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON friendships.friend_id = user2.id;

