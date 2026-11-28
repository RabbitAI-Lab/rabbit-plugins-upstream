/*
 * aiot_types.h - C89 兼容的定宽整数类型
 *
 * C89 没有 <stdint.h>。本 SDK 面向 32 位 MCU（Cortex-M / ARM7/9）和
 * 常见 PC 编译器，直接使用 C89 原生类型：
 *
 *   aiot_u8  = unsigned char
 *   aiot_u16 = unsigned short
 *   aiot_u32 = unsigned int
 *   aiot_i32 = signed int
 *
 * 在 ARM/Keil/IAR/Windows/Linux 上这些都是 8/16/32/32 位。
 * 下面的 typedef 数组会在 unsigned int 不是 32 位时产生编译错误，
 * 避免在 16 位 int 的平台上静默出错。
 */

#ifndef AIOT_TYPES_H
#define AIOT_TYPES_H

typedef unsigned char aiot_u8;
typedef unsigned short aiot_u16;
typedef unsigned int aiot_u32;
typedef signed int aiot_i32;

typedef char aiot_typecheck_u16[(sizeof(aiot_u16) == 2) ? 1 : -1];
typedef char aiot_typecheck_u32[(sizeof(aiot_u32) == 4) ? 1 : -1];

#endif /* AIOT_TYPES_H */
