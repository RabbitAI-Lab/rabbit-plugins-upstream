# OPC UA 安全配置指南

## 安全模型三层架构

```
┌─────────────────────────────────────┐
│           应用层安全                  │
│  用户认证（User Authentication）     │
│  - 用户名/密码                       │
│  - X.509 证书                       │
│  - Kerberos                         │
│  - 匿名                              │
├─────────────────────────────────────┤
│          传输层安全                   │
│  应用认证（Application Authentication）│
│  - X.509 证书双向认证                │
│  消息安全（Message Security）         │
│  - 签名（Sign）                      │
│  - 加密（SignAndEncrypt）            │
├─────────────────────────────────────┤
│           网络层安全                  │
│  - 防火墙规则（端口 4840）            │
│  - VPN / TLS 隧道                    │
└─────────────────────────────────────┘
```

## 安全策略（SecurityPolicy）

| 策略 | 加密强度 | 推荐场景 |
|------|---------|---------|
| None | 无 | 仅限开发/隔离网络测试（不推荐生产） |
| Basic256Sha256 | 256-bit | 兼容性优先 |
| Aes128_Sha256_RsaOaep | 128-bit AES | 平衡性能与安全 |
| **Aes256_Sha256_RsaPss** | 256-bit AES | **生产推荐**（最强） |

## 安全模式（MessageSecurityMode）

| 模式 | 签名 | 加密 | 说明 |
|------|------|------|------|
| None | ❌ | ❌ | 明文传输，不安全 |
| Sign | ✅ | ❌ | 防篡改，不防窃听 |
| **SignAndEncrypt** | ✅ | ✅ | **生产推荐** |

## 连接握手全流程

```
Client                                    Server
  │                                          │
  │──① Hello (请求端点)────────────────────→│
  │←─② Acknowledge (返回端点/安全策略)──────│
  │                                          │
  │──③ OpenSecureChannel (客户端证书)──────→│
  │   服务端验证客户端证书                     │
  │←─④ OpenSecureChannel Response──────────│
  │   客户端验证服务端证书                     │
  │   [证书交换完成，安全通道建立]              │
  │                                          │
  │──⑤ CreateSession (用户凭证)────────────→│
  │←─⑥ CreateSession Response─────────────│
  │                                          │
  │──⑦ ActivateSession────────────────────→│
  │←─⑧ ActivateSession Response───────────│
  │   [会话激活，可以开始通信]                  │
```

## 证书配置

### 创建自签名证书（OpenSSL）

```bash
# 生成私钥
openssl genrsa -out myapp_private.key 2048

# 生成自签名证书（有效期 365 天）
openssl req -new -x509 -key myapp_private.key -out myapp_cert.pem -days 365 \
  -subj "/CN=MyOPCApp/O=MyCompany/C=CN"

# 导出 .der 格式（某些 SDK 需要）
openssl x509 -in myapp_cert.pem -outform der -out myapp_cert.der
```

### Python 客户端证书配置

```python
from asyncua import Client

client = Client(url="opc.tcp://server:4840")
client.set_security(
    policy_strings=["http://opcfoundation.org/UA/SecurityPolicy#Basic256Sha256"],
    certificate="path/to/client_cert.pem",
    private_key="path/to/client_private_key.pem",
)
```

### 信任服务端证书（首次连接处理）

```python
# 方案 1：开发环境自动接受（不用于生产！）
client.set_security(policy_strings=[...])
# 自动信任

# 方案 2：手动信任已知证书
client.set_security(
    policy_strings=[...],
    certificate="client_cert.pem",
    private_key="client_key.pem",
    server_certificate="server_cert.pem"  # 预设信任
)
```

### Node.js 证书配置

```javascript
const client = OPCUAClient.create({
    securityMode: MessageSecurityMode.SignAndEncrypt,
    securityPolicy: SecurityPolicy.Basic256Sha256,
    certificateFile: "path/to/client_cert.pem",
    privateKeyFile: "path/to/client_key.pem",
    // 开发环境：自动信任
    automaticallyAcceptUnknownCertificate: true,  // 仅开发！
});
```

## 常见证书错误

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| **BadSecurityChecksFailed** | 证书不被信任 / 安全策略不匹配 | 1. 检查客户端-服务端安全策略一致 2. 确认证书有效期 3. 在服务端信任客户端证书 |
| **BadCertificateUntrusted** | 对方证书未加入信任列表 | 在服务器的信任存储中添加对方证书 |
| **BadCertificateTimeInvalid** | 证书过期或系统时间不同步 | 1. 检查证书有效期 2. NTP 同步系统时间 |
| **BadCertificateHostNameInvalid** | 证书 CN 与连接地址不匹配 | 用证书中的 CN/DNS 名连接，或重新签发证书 |
| **BadCertificateIssuerTimeInvalid** | CA 证书已过期 | 更新 CA 证书 |
| **BadCertificateRevoked** | 证书已被吊销 | 重新签发证书 |
| **BadCertificateUseNotAllowed** | 证书用途不匹配 | 确认证书 Key Usage 包含 Digital Signature / Key Encipherment |

## 防火墙配置

```
防火墙开放端口:
  TCP 4840  — OPC UA 二进制协议（OPC TCP）
  TCP 443   — OPC UA HTTPS（如使用）
  TCP 4843  — OPC UA HTTPS 备选端口

LDS-ME 发现:
  UDP 4840  — 多播发现

GDS:
  TCP 4840  — 全局发现服务器
```

> ⚠️ 生产环境不建议直接暴露 OPC UA 端口到公网，应通过 VPN 或反向代理。

## 安全最佳实践

### 必须遵守

1. **永远不要在生产环境使用 None 安全模式**
2. **定期轮换证书**（建议 1 年有效期）
3. **使用 NTP 同步所有 OPC UA 节点的时间**
4. **最小权限原则**：用户账号只授予必要权限
5. **开启审计日志**：记录连接、读写、配置变更

### 推荐做法

6. 生产环境使用 CA 签发的证书，而非自签名
7. 使用 GDS 集中管理证书信任链
8. 网络隔离：OPC UA 流量走独立 VLAN
9. 监控异常：失败连接尝试告警
10. 定期安全审计：检查证书有效期、权限配置
