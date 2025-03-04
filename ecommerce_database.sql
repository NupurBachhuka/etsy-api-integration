-- MySQL dump 10.13  Distrib 8.0.37, for macos14 (arm64)
--
-- Host: localhost    Database: Ecommerce_database
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `cart_no` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  PRIMARY KEY (`cart_no`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart_item`
--

DROP TABLE IF EXISTS `cart_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart_item` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `cart_no` int DEFAULT NULL,
  `product_no` int DEFAULT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`item_id`),
  KEY `cart_no` (`cart_no`),
  KEY `product_no` (`product_no`),
  CONSTRAINT `cart_item_ibfk_1` FOREIGN KEY (`cart_no`) REFERENCES `cart` (`cart_no`) ON DELETE CASCADE,
  CONSTRAINT `cart_item_ibfk_2` FOREIGN KEY (`product_no`) REFERENCES `product` (`product_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart_item`
--

LOCK TABLES `cart_item` WRITE;
/*!40000 ALTER TABLE `cart_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `cart_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_id` int NOT NULL,
  `customer_name` varchar(255) NOT NULL,
  `gender` enum('Male','Female','Other') NOT NULL,
  `address` text,
  `phone_no` bigint NOT NULL,
  `cart_num` int DEFAULT NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `phone_no` (`phone_no`),
  UNIQUE KEY `cart_num` (`cart_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock_quantity` int NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops',109.95,50),(2,'Mens Casual Premium Slim Fit T-Shirts ',22.30,50),(3,'Mens Cotton Jacket',55.99,50),(4,'Mens Casual Slim Fit',15.99,50),(5,'John Hardy Women\'s Legends Naga Gold & Silver Dragon Station Chain Bracelet',695.00,50),(6,'Solid Gold Petite Micropave ',168.00,50),(7,'White Gold Plated Princess',9.99,50),(8,'Pierced Owl Rose Gold Plated Stainless Steel Double',10.99,50),(9,'WD 2TB Elements Portable External Hard Drive - USB 3.0 ',64.00,50),(10,'SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s',109.00,50),(11,'Silicon Power 256GB SSD 3D NAND A55 SLC Cache Performance Boost SATA III 2.5',109.00,50),(12,'WD 4TB Gaming Drive Works with Playstation 4 Portable External Hard Drive',114.00,50),(13,'Acer SB220Q bi 21.5 inches Full HD (1920 x 1080) IPS Ultra-Thin',599.00,50),(14,'Samsung 49-Inch CHG90 144Hz Curved Gaming Monitor (LC49HG90DMNXZA) – Super Ultrawide Screen QLED ',999.99,50),(15,'BIYLACLESEN Women\'s 3-in-1 Snowboard Jacket Winter Coats',56.99,50),(16,'Lock and Love Women\'s Removable Hooded Faux Leather Moto Biker Jacket',29.95,50),(17,'Rain Jacket Women Windbreaker Striped Climbing Raincoats',39.99,50),(18,'MBJ Women\'s Solid Short Sleeve Boat Neck V ',9.85,50),(19,'Opna Women\'s Short Sleeve Moisture',7.95,50),(20,'DANVOUY Womens T Shirt Casual Cotton Short',12.99,50);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-04 18:45:05
