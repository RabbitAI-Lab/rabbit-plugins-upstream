//go:build windows

package main

import "syscall"

// Windows 控制台默认 GBK，中文和 NBSP 会乱码/崩溃；切成 UTF-8 输出。
func init() {
	kernel32 := syscall.NewLazyDLL("kernel32.dll")
	_, _, _ = kernel32.NewProc("SetConsoleOutputCP").Call(65001)
	_, _, _ = kernel32.NewProc("SetConsoleCP").Call(65001)
}
