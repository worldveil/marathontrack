# ************************************************************
# Sequel Pro SQL dump
# Version 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: sql.mit.edu (MySQL 5.1.66-0+squeeze1-log)
# Database: drevo+marathon
# Generation Time: 2014-04-19 16:22:12 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table group_membership
# ------------------------------------------------------------

DROP TABLE IF EXISTS `group_membership`;

CREATE TABLE `group_membership` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `runner_id` int(11) unsigned NOT NULL,
  `group_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_runner_group` (`runner_id`,`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;



# Dump of table groups
# ------------------------------------------------------------

DROP TABLE IF EXISTS `groups`;

CREATE TABLE `groups` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '',
  `passphrase` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;



# Dump of table progress_updates
# ------------------------------------------------------------

DROP TABLE IF EXISTS `progress_updates`;

CREATE TABLE `progress_updates` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `runner_id` int(11) NOT NULL,
  `location_km` int(11) DEFAULT NULL,
  `race_starttime` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `elapsed_time_seconds` int(11) NOT NULL,
  `string_location` varchar(50) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;



# Dump of table runners
# ------------------------------------------------------------

DROP TABLE IF EXISTS `runners`;

CREATE TABLE `runners` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `first` int(30) NOT NULL,
  `last` int(30) NOT NULL,
  `gender` varchar(1) NOT NULL DEFAULT '',
  `city` varchar(30) NOT NULL DEFAULT '',
  `state` varchar(20) NOT NULL DEFAULT '',
  `bib_number` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_bib` (`bib_number`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
