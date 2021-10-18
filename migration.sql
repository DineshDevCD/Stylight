ALTER TABLE `stylight`.`t_budgets` 
ADD COLUMN `a_notification` TINYINT(1) NOT NULL DEFAULT 0 AFTER `a_amount_spent`;