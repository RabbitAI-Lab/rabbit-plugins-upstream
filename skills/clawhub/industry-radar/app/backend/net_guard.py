"""
出站抓取的统一安全出口（SSRF 防护）。

背景
----
本服务的正文页 URL 来自 RSS 条目、也就是**外部可控内容**。若直接
`requests.get(article_url)`，攻击者只要在源里塞一条指向
`http://169.254.169.254/...`（云元数据）或 `http://10.0.0.5:8080/`
（内网服务）的链接，就能借服务端身份去访问内网。

策略（默认拒绝）
----
1. 只允许 http / https，其余协议（file://、gopher://、ftp://…）一律拒绝。
2. 拒绝携带 userinfo 的 URL（`http://a:b@host`），避免解析歧义。
3. 主机名先按字面判断，再做 DNS 解析，**所有**解析结果必须落在公网地址段，
   否则拒绝——命中回环、私网、链路本地（含 169.254.169.254 元数据）、
   CGNAT、保留段、组播、IPv6 ULA / link-local 都要拦。
4. 不自动跟随重定向：手动逐跳跟随（最多 MAX_REDIRECTS 次），
   每一跳都重新走第 1~3 步，防止「公网 302 到内网」绕过。
5. 响应体限量读取（默认 3MB），避免被超大响应拖垮。

残余风险与生产建议
----
DNS 在「校验」与「连接」之间仍可能被重绑定（TOCTOU）。本模块把该窗口压到
最小，但彻底的方案是出网白名单 / 正向代理；云上部署时应在 VPC 侧配置
Security Group + NAT 白名单，禁止访问 169.254.169.254 与内网网段。
"""
from __future__ import annotations

import ipaddress
import logging
import os
import socket
from typing import Dict, Optional, Set
from urllib.parse import urljoin, urlparse

import requests

log = logging.getLogger("industryradar.netguard")

ALLOWED_SCHEMES = ("http", "https")
MAX_REDIRECTS = 3
DEFAULT_MAX_BYTES = 3 * 1024 * 1024


class UnsafeUrlError(ValueError):
    """URL 未通过出站安全校验。"""


# 明确禁止的地址段（含云元数据、回环、私网、保留、组播）
_BLOCKED_NETWORKS = tuple(ipaddress.ip_network(n) for n in (
    "0.0.0.0/8",          # 本网络
    "10.0.0.0/8",         # 私网 A
    "100.64.0.0/10",      # CGNAT（云厂商内部常用）
    "127.0.0.0/8",        # 回环
    "169.254.0.0/16",     # 链路本地：169.254.169.254 云元数据
    "172.16.0.0/12",      # 私网 B
    "192.0.0.0/24",       # IETF 协议分配
    "192.0.2.0/24",       # TEST-NET-1
    "192.168.0.0/16",     # 私网 C
    "198.51.100.0/24",    # TEST-NET-2
    "203.0.113.0/24",     # TEST-NET-3
    "224.0.0.0/4",        # 组播
    "240.0.0.0/4",        # 保留 + 广播
    "::/128", "::1/128",  # 未指定 / 回环
    "fc00::/7",           # IPv6 ULA
    "fe80::/10",          # IPv6 链路本地
    "ff00::/8",           # IPv6 组播
    "64:ff9b::/96",       # NAT64（可映射到内网 v4）
))

# 本地代理（如 Clash fake-IP 模式）会把所有域名解析到 198.18.0.0/15。
# 该段不可路由、也到不了任何内网/元数据地址，因此默认放行，否则本地演示
# 环境（挂在代理后）会抓不到任何正文。生产环境可置 IR_BLOCK_PROXY_FAKEIP=1。
_PROXY_FAKEIP_NET = ipaddress.ip_network("198.18.0.0/15")
_BLOCK_PROXY_FAKEIP = os.getenv("IR_BLOCK_PROXY_FAKEIP", "0") == "1"

# IPv6 里包裹的 IPv4（NAT64 / IPv4-translated），必须拆开再判段，
# 否则 ::ffff:127.0.0.1 之类的写法能绕过检查。
_NAT64_NETS = (
    ipaddress.ip_network("64:ff9b::/96"),
    ipaddress.ip_network("::ffff:0:0:0/96"),
)

_BLOCKED_HOSTNAMES = {
    "localhost", "localhost.localdomain", "ip6-localhost", "ip6-loopback",
    "metadata", "metadata.google.internal", "instance-data",
}
_BLOCKED_SUFFIXES = (".localhost", ".local", ".internal", ".home.arpa")


def _strip_zone(addr: str) -> str:
    """去掉 IPv6 的 scope id（fe80::1%eth0 → fe80::1）。"""
    return addr.split("%", 1)[0]


def _unwrap_v4(ip):
    """把 IPv6 里包裹的 IPv4 拆出来（::ffff:a.b.c.d / NAT64 / v4-translated）。"""
    if not isinstance(ip, ipaddress.IPv6Address):
        return ip
    if ip.ipv4_mapped is not None:
        return ip.ipv4_mapped
    for net in _NAT64_NETS:
        if ip in net:
            return ipaddress.IPv4Address(int(ip) & 0xFFFFFFFF)
    return ip


def is_public_ip(addr: str) -> bool:
    """判断单个 IP 字面量是否为可访问的公网地址。"""
    try:
        ip = _unwrap_v4(ipaddress.ip_address(_strip_zone(addr)))
    except ValueError:
        return False

    # fake-IP 代理段：默认视为可用公网出口（详见 _PROXY_FAKEIP_NET 说明）
    if isinstance(ip, ipaddress.IPv4Address) and ip in _PROXY_FAKEIP_NET \
            and not _BLOCK_PROXY_FAKEIP:
        return True

    if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved \
            or ip.is_multicast or ip.is_unspecified:
        return False
    return not any(ip in net for net in _BLOCKED_NETWORKS if net.version == ip.version)


def _resolve(host: str) -> Set[str]:
    """解析主机名，返回全部 A/AAAA 地址；解析失败返回空集。"""
    try:
        infos = socket.getaddrinfo(host, None, type=socket.SOCK_STREAM)
    except socket.gaierror as exc:
        log.debug("dns resolve failed: %s (%s)", host, exc)
        return set()
    return {_strip_zone(info[4][0]) for info in infos}


def check_url(url: str) -> str:
    """校验 URL 是否允许出站；通过返回原 URL，否则抛 UnsafeUrlError。"""
    raw = (url or "").strip()
    if not raw:
        raise UnsafeUrlError("空 URL")

    try:
        p = urlparse(raw)
    except ValueError as exc:
        raise UnsafeUrlError(f"URL 无法解析: {raw!r}") from exc

    if p.scheme.lower() not in ALLOWED_SCHEMES:
        raise UnsafeUrlError(f"不允许的协议: {p.scheme or '(none)'}")
    if p.username or p.password:
        raise UnsafeUrlError("URL 不允许携带用户凭证")

    host = (p.hostname or "").strip().lower().rstrip(".")
    if not host:
        raise UnsafeUrlError("URL 缺少主机名")
    if host in _BLOCKED_HOSTNAMES or host.endswith(_BLOCKED_SUFFIXES):
        raise UnsafeUrlError(f"禁止访问的主机: {host}")

    # 字面量 IP：直接判段
    try:
        literal = ipaddress.ip_address(_strip_zone(host))
    except ValueError:
        literal = None

    if literal is not None:
        if not is_public_ip(str(literal)):
            raise UnsafeUrlError(f"禁止访问的地址: {host}")
        return raw

    # 域名：解析后所有地址都必须是公网地址（有任一内网结果即拒绝）
    addrs = _resolve(host)
    if not addrs:
        raise UnsafeUrlError(f"域名无法解析: {host}")
    for addr in addrs:
        if not is_public_ip(addr):
            raise UnsafeUrlError(f"域名解析到内网地址: {host} -> {addr}")
    return raw


def is_fetchable(url: str) -> bool:
    """check_url 的布尔版，便于调用方提前短路。"""
    try:
        check_url(url)
        return True
    except UnsafeUrlError as exc:
        log.warning("blocked outbound url: %s (%s)", url, exc)
        return False


class SafeResponse:
    """受限响应对象，接口与 requests.Response 的最小子集兼容。"""

    __slots__ = ("status_code", "headers", "content", "url", "_encoding")

    def __init__(self, status_code: int, headers: Dict[str, str], content: bytes, url: str) -> None:
        self.status_code = status_code
        self.headers = headers
        self.content = content
        self.url = url
        self._encoding = None
        ctype = (headers.get("content-type") or "").lower()
        for part in ctype.split(";"):
            part = part.strip()
            if part.startswith("charset="):
                self._encoding = part.split("=", 1)[1].strip("\"'")

    @property
    def text(self) -> str:
        if self._encoding:
            try:
                return self.content.decode(self._encoding, errors="replace")
            except LookupError:
                pass
        return self.content.decode("utf-8", errors="replace")

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise requests.HTTPError(f"{self.status_code} for url: {self.url}")


def safe_get(
    url: str,
    *,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 15,
    max_bytes: int = DEFAULT_MAX_BYTES,
    max_redirects: int = MAX_REDIRECTS,
) -> SafeResponse:
    """带 SSRF 校验的 GET。每一跳都校验；超限截断；重定向手动跟随。"""
    current = check_url(url)

    for _ in range(max_redirects + 1):
        resp = requests.get(
            current, headers=headers, timeout=timeout,
            allow_redirects=False, stream=True,
        )
        try:
            status = resp.status_code
            location = resp.headers.get("Location")
            if status in (301, 302, 303, 307, 308) and location:
                current = check_url(urljoin(current, location))  # 跳转目标重新校验
                continue

            chunks: list[bytes] = []
            total = 0
            for chunk in resp.iter_content(8192):
                if not chunk:
                    continue
                chunks.append(chunk)
                total += len(chunk)
                if total >= max_bytes:
                    log.warning("response truncated at %d bytes: %s", total, current)
                    break
            return SafeResponse(status, dict(resp.headers), b"".join(chunks)[:max_bytes], current)
        finally:
            resp.close()

    raise UnsafeUrlError(f"重定向次数超过上限 ({max_redirects}): {url}")
