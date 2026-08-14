# 错误处理

错误信息输出到 stderr，程序 exit code 为 1：

```bash
kugou-cli music search "xxx" 2>&1
echo $?  # 非 0 表示出错
```

---

## 常见错误及处理

| 错误信息 | 原因 | 处理方式 |
|---------|------|---------|
| `账号登录过期，请重新登录` | 登录态已过期（errcode 语义由上游约定）。CLI 已**自动**清理本地登录态 | 引导用户重新登录：`kugou-cli auth login`（扫码）或 `kugou-cli auth set-secret "<新 secret>"` |
| `not logged in` / `auth file not found` | 未登录 | 引导用户执行 `kugou-cli auth login` |
| `HTTP error: 400` | 请求参数有误 | 检查命令参数是否正确 |
| `HTTP error: 500` | 服务端错误 | 稍后重试，或告知用户 |
| `API error: <errmsg> (code=<N>)` | 业务错误（上游 errcode ≠ 0） | 根据 errmsg 提示用户 |
| `network error: ...` | 网络连接问题 | 检查网络，可尝试 `--proxy` |
| `failed to get device info` | 设备信息获取失败（仅 control） | 运行时环境异常，检查权限 |
