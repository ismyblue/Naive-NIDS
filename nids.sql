BEGIN;
--
-- Create model FullEvent
--
CREATE TABLE `fullevent` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `sig_name` varchar(255) NOT NULL, `sig_priority` int unsigned NOT NULL, `timestamp` datetime NOT NULL, `ip_src`
int unsigned NOT NULL, `ip_dst` int unsigned NOT NULL, `ip_proto` int unsigned NOT NULL, `port_src` int unsigned NOT NULL, `port_dst` int unsigned NOT NULL);
--
-- Create model Role
--
CREATE TABLE `roles` (`role_id` integer AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY, `role_name` varchar(20) NOT NULL, `role_desc` varchar(75) NOT NULL);
--
-- Create model User
--
CREATE TABLE `users` (`usr_id` integer AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY, `usr_login` varchar(25) NOT NULL, `usr_pwd` varchar(32) NOT NULL, `usr_name` varchar(75) NOT NULL, `usr_enab
led` integer NOT NULL, `role_id` integer NOT NULL);
--
-- Add field cid to fullevent
--
ALTER TABLE `fullevent` ADD COLUMN `cid` int unsigned NOT NULL;
--
-- Add field sid to fullevent
--
ALTER TABLE `fullevent` ADD COLUMN `sid` int unsigned NOT NULL;
--
-- Add field sig_class_id to fullevent
--
ALTER TABLE `fullevent` ADD COLUMN `sig_class_id` int unsigned NOT NULL;
--
-- Add field signature to fullevent
--
ALTER TABLE `fullevent` ADD COLUMN `signature` int unsigned NOT NULL;
--
-- Alter unique_together for data (1 constraint(s))
--
ALTER TABLE `users` ADD CONSTRAINT `users_role_id_fd07f6e4_fk_roles_role_id` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`);
CREATE INDEX `users_role_id_fd07f6e4` ON `users` (`role_id`);
CREATE INDEX `fullevent_cid_aabcc0f1` ON `fullevent` (`cid`);
ALTER TABLE `fullevent` ADD CONSTRAINT `fullevent_cid_aabcc0f1_fk_event_cid` FOREIGN KEY (`cid`) REFERENCES `event` (`cid`);
CREATE INDEX `fullevent_sid_e51cc098` ON `fullevent` (`sid`);
ALTER TABLE `fullevent` ADD CONSTRAINT `fullevent_sid_e51cc098_fk_sensor_sid` FOREIGN KEY (`sid`) REFERENCES `sensor` (`sid`);
CREATE INDEX `fullevent_sig_class_id_9165b915` ON `fullevent` (`sig_class_id`);
ALTER TABLE `fullevent` ADD CONSTRAINT `fullevent_sig_class_id_9165b915_fk_sig_class_sig_class_id` FOREIGN KEY (`sig_class_id`) REFERENCES `sig_class` (`sig_class_id`);
CREATE INDEX `fullevent_signature_a968ca0f` ON `fullevent` (`signature`);
ALTER TABLE `fullevent` ADD CONSTRAINT `fullevent_signature_a968ca0f_fk_signature_sig_id` FOREIGN KEY (`signature`) REFERENCES `signature` (`sig_id`);
COMMIT;