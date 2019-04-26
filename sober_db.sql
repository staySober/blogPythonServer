/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50725
 Source Host           : localhost:3306
 Source Schema         : sober

 Target Server Type    : MySQL
 Target Server Version : 50725
 File Encoding         : 65001

 Date: 26/04/2019 19:07:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for blog
-- ----------------------------
DROP TABLE IF EXISTS `blog`;
CREATE TABLE `blog`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `create_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  `update_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `id_key`(`id`) USING BTREE,
  INDEX `type_key`(`type`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of blog
-- ----------------------------
INSERT INTO `blog` VALUES (1, '第一篇博客', '# 这是 H1 #\r\n\r\n## 这是 H2 ##\r\n\r\n### 这是 H3 ######12313413414那么热欸融合案说法都发发<br><br><a>点我</a>', 'java', '2019-04-25 19:13:28', '2019-04-26 14:32:38');
INSERT INTO `blog` VALUES (2, '第六篇博客', '# 这是 H1 #\r\n\r\n## 这是 H2 ##\r\n\r\n### 这是 H3 ######12313413414那么热欸融合案说法都发发<br><br><a>点我</a>', 'jenkins', '2019-04-25 19:13:28', '2019-04-26 14:32:41');
INSERT INTO `blog` VALUES (3, '第二篇博客', '# 这是 H1 #\r\n\r\n## 这是 H2 ##\r\n\r\n### 这是 H3 ######12313413414那么热欸融合案说法都发发<br><br><a>点我</a>', 'react', '2019-04-25 19:13:28', '2019-04-26 14:32:43');
INSERT INTO `blog` VALUES (4, '第三篇博客', '# 这是 H1 #\r\n\r\n## 这是 H2 ##\r\n\r\n### 这是 H3 ######12313413414那么热欸融合案说法都发发<br><br><a>点我</a>', 'vue', '2019-04-25 19:13:28', '2019-04-26 14:32:46');
INSERT INTO `blog` VALUES (5, '第四篇博客', '# 这是 H1 #\r\n\r\n## 这是 H2 ##\r\n\r\n### 这是 H3 ######\r\n12313413414那么热欸融合案说法都发发<br><br><a>点我</a>', 'python', '2019-04-25 19:13:28', '2019-04-26 14:32:48');
INSERT INTO `blog` VALUES (6, '第五篇博客', '# 这是 H1 #\r\n\r\n## 这是 H2 ##\r\n\r\n### 这是 H3 ######\r\n12313413414那么热欸融合案说法都发发<br><br><a>点我</a>', 'java', '2019-04-25 19:13:28', '2019-04-26 14:32:50');

-- ----------------------------
-- Table structure for type
-- ----------------------------
DROP TABLE IF EXISTS `type`;
CREATE TABLE `type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of type
-- ----------------------------
INSERT INTO `type` VALUES (1, 'java');
INSERT INTO `type` VALUES (2, 'python');
INSERT INTO `type` VALUES (3, 'react');
INSERT INTO `type` VALUES (4, 'vue');
INSERT INTO `type` VALUES (5, 'jenkins');

SET FOREIGN_KEY_CHECKS = 1;
