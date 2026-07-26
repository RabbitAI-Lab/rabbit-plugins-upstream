# OPC UA 故障排查手册

## 四步排查法

```
1. 确认症状 → 2. 定位层级 → 3. 匹配根因 → 4. 验证修复
```

### 排查层级

```
应用层：读写失败、数据异常、订阅不工作
  ↓
会话层：BadSessionIdInvalid、会话超时
  ↓
安全层：BadSecurityChecksFailed、证书错误
  ↓
传输层：连接超时、Connection Refused、端口不通
  ↓
网络层：防火墙拦截、DNS 解析失败
```

---

## 连接类问题

### 1. 连接超时 (Connection Timeout)

**症状**：客户端一直等待，最终超时

**排查步骤**：
```bash
# 1. 确认端口可达
telnet <server_ip> 4840
# 或
nc -zv <server_ip> 4840

# 2. 确认服务器在监听
netstat -an | findstr 4840  # Windows
netstat -an | grep 4840      # Linux

# 3. 防火墙检查
# Windows
netsh advfirewall firewall show rule name=all | findstr 4840
# Linux
iptables -L -n | grep 4840
```

**常见原因**：
- 防火墙拦截 TCP 4840 端口
- 服务器未启动或崩溃
- 端点 URL 格式错误（需 `opc.tcp://` 而非 `http://`）
- 网络不通（跨网段需路由配置）

**解决方案**：
1. 检查并开放防火墙规则
2. 确认服务器进程在运行
3. 检查 URL 格式：`opc.tcp://<IP>:<port>`
4. `ping <server_ip>` 测试基础网络

### 2. 连接被拒绝 (Connection Refused)

**症状**：`ConnectionRefused` 或 `ECONNREFUSED`

**原因与方案**：
| 原因 | 解决方案 |
|------|---------|
| 端口号错误 | 用 UaExpert 扫描确认实际端口 |
| 服务器已达最大连接数 | 增加 MaxSessionCount 配置 |
| 服务器仅监听 localhost | 修改配置绑定 0.0.0.0 |
| IP 地址不匹配 | 确认服务器网卡绑定正确 |

### 3. 端点未找到 (Endpoint Not Found)

**症状**：`BadTcpEndpointUrlInvalid` / `BadNotFound`

**原因**：
- Discovery URL 与实际端点路径不一致
- LDS 注册信息过期

**解决**：
```bash
# 使用 discovery URL 获取端点
# 正确格式：
opc.tcp://192.168.1.100:4840  # 自动发现
# 而非直接指定完整路径（除非你确定）：
opc.tcp://192.168.1.100:4840/SomeSpecificPath
```

---

## 证书与安全类问题

### 4. BadSecurityChecksFailed

**症状**：连接建立后立即断开，或读写操作返回此错误

**排查清单**：
- [ ] 客户端和服务端的安全策略是否匹配？
- [ ] 客户端证书是否已被服务端信任？
- [ ] 服务端证书是否已被客户端信任？
- [ ] 证书是否在有效期内？
- [ ] 系统时间是否同步（NTP）？
- [ ] 证书的 ApplicationUri 是否匹配？

**典型场景与解决**：

**场景 A — 首次连接被拒绝**
```
1. 用 None 安全模式先测试网络连通性
2. 确认连通后，切换到 Sign / SignAndEncrypt
3. 首次安全连接会被拒绝（证书交换阶段）
4. 在服务端管理界面找到被拒绝的客户端证书
5. 手动将其加入信任列表
6. 重新连接
```

**场景 B — open62541 v1.4+ 升级后连接失败**
```
open62541 从 1.3 升级到 1.4 后，None 模式也强制验证证书。
解决方案：
- 方案 1：正确配置证书信任（推荐）
- 方案 2：同 v1.3 行为，需要修改服务器配置放宽验证
```

**场景 C — Python opcua 库加密连接失败**
```python
# 确保客户端和服务端使用相同的安全策略
client.set_security(
    policy_strings=["http://opcfoundation.org/UA/SecurityPolicy#Basic256Sha256"]
)
# 检查路径是否正确
client.load_client_certificate("path/to/cert.pem")
client.load_private_key("path/to/key.pem")
```

### 5. BadCertificateUntrusted

**通用解决流程**：
1. **UaExpert**：弹窗 → Trust Server Certificate → 继续
2. **Prosys Server**：管理界面 → Certificates → Rejected → 右键 trust
3. **Kepware**：OPC UA Configuration → Trusted Clients → Import
4. **Siemens S7-1500**：TIA Portal → CPU OPC UA 设置 → 信任客户端证书
5. **open62541**：将 DER 证书放到服务器的 `trusted/certs/` 目录

---

## 数据访问类问题

### 6. BadNodeIdUnknown

**症状**：读取/写入时返回此状态码

**排查**：
```python
# 先浏览确认节点是否存在
browser = client.get_objects_node()
for child in browser.get_children():
    print(f"NodeId: {child.nodeid}, Name: {child.get_browse_name().Name}")
```

**常见原因**：
- NodeId 拼写错误
- 命名空间索引 (ns=) 错误
- 节点已被删除或重命名
- 服务器重启后动态 NodeId 变化

### 7. BadNotWritable / BadUserAccessDenied

**原因**：权限不足

**解决方案**：
1. 检查当前用户是否有写权限
2. 检查节点的 AccessLevel 属性
3. 使用有写权限的用户重新创建会话
4. Admin 登录检查 UserAccessLevel

### 8. BadWaitingForInitialData / BadNoData

**症状**：订阅创建后没有数据推送

**排查清单**：
- [ ] 监控项的 Publishing Interval 是否太长？
- [ ] 节点是否有实际数据变化？
- [ ] 订阅的 MaxKeepAliveCount 是否合理？
- [ ] 客户端订阅回调是否正确注册？

```python
# 正确的订阅设置
handler = SubHandler()
sub = await client.create_subscription(100, handler)  # 100ms 发布间隔
handle = await sub.subscribe_data_change(
    node,
    MonitoringMode.Reporting,
    DeadbandType.Percent,  # 死区类型
    0.0,                    # 死区值
    DataChangeTrigger.StatusValueTimestamp
)
```

---

## 性能类问题

### 9. 订阅数量过大导致性能下降

**优化策略**：
- 合并相近监控项到一个订阅
- 增大 Publishing Interval（如 100ms → 500ms）
- 使用死区（Deadband）过滤无明显变化的数据
- 批量读写代替单次操作

### 10. 连接频繁断开

**原因与方案**：
| 原因 | 表现 | 方案 |
|------|------|------|
| 会话超时 | 空闲一段时间后断开 | 增大 SessionTimeout |
| 网络不稳定 | 随机断开 | 实现自动重连逻辑 |
| 服务器资源不足 | 负载高时断开 | 优化服务器配置/扩容 |
| KeepAlive 丢失 | 无操作也断开 | 调整 KeepAlive 间隔 |

```python
# 自动重连示例（opcua-asyncio）
import asyncio
from asyncua import Client

async def connect_with_retry(url, max_retries=5, retry_delay=5):
    for attempt in range(max_retries):
        try:
            client = Client(url=url)
            await client.connect()
            print(f"连接成功 (尝试 {attempt+1}/{max_retries})")
            return client
        except Exception as e:
            print(f"连接失败 (尝试 {attempt+1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(retry_delay)
    raise ConnectionError(f"无法连接到 {url}，已重试 {max_retries} 次")
```

---

## 诊断工具速查

| 工具 | 用途 | 获取方式 |
|------|------|---------|
| **UaExpert** | 通用 OPC UA 客户端，浏览/读写/订阅 | 免费注册下载 |
| **Prosys OPC UA Browser** | 轻量级浏览器，快速验证连接 | 免费 |
| **Wireshark** | 抓包分析 OPC UA 协议交互 | 开源免费 |
| **OPC Foundation Sample Client** | 官方示例，参考实现 | GitHub |
| **openssl** | 证书生成、查看、验证 | 系统自带/安装 |

### Wireshark 抓 OPC UA 包

```bash
# 过滤 OPC UA 流量
opcua

# 只看连接建立
opcua.msgtype == "HEL" or opcua.msgtype == "ACK" or opcua.msgtype == "OPN"

# 看具体数据读写
opcua.servicenodeid
```

---

## 紧急情况快速决策

```
1. 完全连不上？
   → telnet/nc 测试端口 → 检查防火墙 → 检查服务端进程

2. 能连上但证书报错？
   → 先用 None 模式验证 → 检查双方证书信任 → 对时(NTP)

3. 连上了但读不到数据？
   → 浏览地址空间 → 确认 NodeId 正确 → 检查权限

4. 订阅没数据？
   → 检查发布间隔 → 确认数据有变化 → 检查回调注册

5. 连接不稳定？
   → 增加超时 → 实现重连 → 检查网络质量
```
