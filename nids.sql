BEGIN;
--
-- Create model FullEvent
--
CREATE TABLE `fullevent` (`sid` int unsigned NOT NULL PRIMARY KEY, `cid` int unsigned NOT NULL, `signature` int unsigned NOT NULL, `sig_name` varchar(255) NOT NULL, `sig_class_id` int unsig
ned NOT NULL, `sig_priority` int unsigned NOT NULL, `timestamp` datetime NOT NULL, `ip_src` int unsigned NOT NULL, `ip_dst` int unsigned NOT NULL, `ip_proto` integer NOT NULL, `port_src` in
t unsigned NOT NULL, `port_dst` int unsigned NOT NULL);
--
-- Create model Role
--
CREATE TABLE `role` (`role_id` integer NOT NULL PRIMARY KEY, `role_name` varchar(20) NOT NULL, `role_desc` varchar(75) NOT NULL);
--
-- Create model User
--
CREATE TABLE `user` (`usr_id` integer NOT NULL PRIMARY KEY, `usr_login` varchar(25) NOT NULL, `usr_pwd` varchar(32) NOT NULL, `usr_name` varchar(75) NOT NULL, `role_id` integer NOT NULL, `u
sr_enabled` integer NOT NULL);
COMMIT;
