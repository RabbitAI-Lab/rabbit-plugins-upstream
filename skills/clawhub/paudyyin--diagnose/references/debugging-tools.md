# 调试工具指南

## 调试器

### Node.js / JavaScript
- **VSCode Debugger** — launch.json配置，支持attach到运行进程
- **node --inspect** — 启动inspect协议，Chrome DevTools连接
- **ndb** — Google出品的Node调试器包装

### Python
- **pdb / pdb++** — 内置调试器，pdb++增强版
- **breakpoint()** — Python 3.7+内置断点函数
- **VSCode Python Debugger** — 图形化调试

### Go
- **dlv (Delve)** — Go标准调试器
- **go test -run** — 配合测试运行调试

### Java / JVM
- **jdb** — JDK内置调试器
- **IDEA/Eclipse远程调试** — 支持远程attach

## 性能分析工具

### CPU Profiling
| 语言 | 工具 | 用法 |
|------|------|------|
| JavaScript | `--prof` / Chrome DevTools | `node --prof app.js` |
| Python | `cProfile` / `py-spy` | `python -m cProfile app.py` |
| Go | `pprof` | `go test -cpuprofile=cpu.prof` |
| Java | `async-profiler` / JFR | 生产环境推荐async-profiler |

### Memory Profiling
| 语言 | 工具 | 用法 |
|------|------|------|
| JavaScript | Chrome DevTools Memory | Heap snapshot对比 |
| Python | `tracemalloc` / `memory_profiler` | 逐行内存追踪 |
| Go | `pprof` heap | `go test -memprofile=mem.prof` |
| Java | `jmap` / VisualVM | Heap dump分析 |

### 数据库查询分析
- **PostgreSQL**: `EXPLAIN ANALYZE` — 显示实际执行计划和耗时
- **MySQL**: `EXPLAIN` — 显示查询执行计划
- **MongoDB**: `.explain("executionStats")` — 查询性能分析

## 日志工具

### 结构化日志
```
# 推荐格式
[LEVEL-timestamp-component] message {key: value}

# 示例
[INFO-2026-06-20T08:00:00-auth] login success {user: "admin", ip: "10.0.0.1"}
[DEBUG-a4f2-2026-06-20T08:00:01-parser] token mismatch {expected: "}", got: "EOF"}
```

### 日志级别使用
| 级别 | 用途 | 生产环境 |
|------|------|---------|
| ERROR | 需要立即关注的错误 | ✅ 保留 |
| WARN | 潜在问题，不影响功能 | ✅ 保留 |
| INFO | 关键业务流程节点 | ✅ 保留 |
| DEBUG | 调试信息 | ❌ 关闭（调试时开启） |
| TRACE | 极详细的追踪 | ❌ 关闭 |

## 网络调试

### HTTP抓包
- **curl -v** — 查看完整HTTP请求/响应
- **httpie** — 更友好的HTTP客户端
- **Chrome DevTools Network** — 浏览器网络请求分析

### API测试
- **Postman / Insomnia** — API测试集合
- **k6 / wrk** — 负载测试
- **mitmproxy** — 中间人代理，拦截和修改HTTP流量

## 系统级工具

### Linux
- `strace` — 系统调用追踪
- `ltrace` — 库调用追踪
- `perf` — 性能分析
- `tcpdump` / `wireshark` — 网络包分析
- `dmesg` — 内核日志

### Windows
- **Process Monitor** — 文件/注册表/网络活动监控
- **DebugView** — 查看Debug输出
- **Performance Monitor** — 系统性能计数器
- **Wireshark** — 网络包分析
