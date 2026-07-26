"""
OPC UA 实用工具函数
用途：提供 OPC UA 连接验证、地址空间浏览、证书生成等常用工具函数

依赖：pip install opcua-asyncio
"""

import asyncio
import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime


# ============================================================
# 1. 连接性检查
# ============================================================

def check_port(host: str, port: int = 4840, timeout: float = 5.0) -> dict:
    """
    检查 OPC UA 服务器端口是否可达

    Args:
        host: 服务器 IP 或主机名
        port: 端口号，默认 4840
        timeout: 超时秒数

    Returns:
        {"reachable": bool, "host": str, "port": int, "error": str|None}
    """
    import socket

    result = {"reachable": False, "host": host, "port": port, "error": None}
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        ret = sock.connect_ex((host, port))
        sock.close()
        if ret == 0:
            result["reachable"] = True
        else:
            result["error"] = f"连接失败，错误码: {ret}"
    except socket.gaierror as e:
        result["error"] = f"DNS 解析失败: {e}"
    except socket.timeout:
        result["error"] = f"连接超时 ({timeout}s)"
    except Exception as e:
        result["error"] = str(e)

    return result


# ============================================================
# 2. OPC UA 服务器发现
# ============================================================

async def discover_endpoints(url: str) -> list[dict]:
    """
    发现 OPC UA 服务器的端点信息

    Args:
        url: Discovery URL，如 "opc.tcp://192.168.1.100:4840"

    Returns:
        端点信息列表，每个端点包含 endpoint_url, security_policy, security_mode 等
    """
    try:
        from asyncua import Client
    except ImportError:
        print("请先安装 opcua-asyncio: pip install opcua-asyncio")
        return []

    endpoints_info = []
    try:
        async with Client(url=url, timeout=5) as client:
            endpoints = client.server_urls
            print(f"发现 {len(endpoints)} 个端点:")
            for ep in endpoints:
                info = {"endpoint_url": ep}
                endpoints_info.append(info)
    except Exception as e:
        print(f"发现失败: {e}")

    return endpoints_info


# ============================================================
# 3. 地址空间浏览
# ============================================================

async def browse_address_space(
    url: str,
    start_node: str = "ObjectsFolder",
    max_depth: int = 3,
    show_values: bool = False,
) -> None:
    """
    浏览 OPC UA 服务器的地址空间树状结构

    Args:
        url: 服务器端点 URL
        start_node: 起始节点，可选 "Root"/"ObjectsFolder"/"TypesFolder"/"ViewsFolder"
        max_depth: 最大递归深度
        show_values: 是否尝试读取并显示变量值
    """
    try:
        from asyncua import Client
    except ImportError:
        print("请先安装 opcua-asyncio: pip install opcua-asyncio")
        return

    async def _browse(client, node, depth: int, prefix: str = ""):
        if depth > max_depth:
            return
        try:
            children = await node.get_children()
            for child in children:
                try:
                    name = (await child.read_browse_name()).Name
                    node_class = (await child.read_node_class()).name
                    line = f"{prefix}├─ {name} [{node_class}]"

                    if show_values and node_class == "Variable":
                        try:
                            val = await child.read_value()
                            line += f" = {val}"
                        except Exception:
                            line += " = <无法读取>"

                    print(line)
                    await _browse(client, child, depth + 1, prefix + "│  ")
                except Exception as e:
                    print(f"{prefix}├─ <错误: {e}>")
        except Exception as e:
            print(f"{prefix}浏览失败: {e}")

    print(f"正在连接 {url} ...")
    try:
        async with Client(url=url, timeout=5) as client:
            print("连接成功！\n")

            # 选择起始节点
            node_map = {
                "Root": client.get_root_node(),
                "ObjectsFolder": client.get_objects_node(),
                "TypesFolder": client.get_types_node(),
                "ViewsFolder": client.get_views_node(),
            }

            start = await node_map.get(start_node, client.get_objects_node())
            start_name = (await start.read_browse_name()).Name
            print(f"起始节点: {start_name}\n")
            await _browse(client, start, 0)
    except Exception as e:
        print(f"连接失败: {e}")


# ============================================================
# 4. 自签名证书生成
# ============================================================

def generate_self_signed_cert(
    output_dir: str = ".",
    common_name: str = "MyOPCApp",
    org: str = "MyCompany",
    country: str = "CN",
    days: int = 365,
) -> dict:
    """
    使用 OpenSSL 生成 OPC UA 自签名证书

    Args:
        output_dir: 证书输出目录
        common_name: 证书 CN（通用名称）
        org: 组织名称
        country: 国家代码（2 字母）
        days: 证书有效期（天）

    Returns:
        {"cert_pem": str, "key_pem": str, "cert_der": str, "key_der": str} 或包含 error
    """
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    cert_pem = out / f"{common_name}_cert.pem"
    key_pem = out / f"{common_name}_key.pem"
    cert_der = out / f"{common_name}_cert.der"
    key_der = out / f"{common_name}_key.der"

    subject = f"/CN={common_name}/O={org}/C={country}"

    result = {
        "cert_pem": str(cert_pem),
        "key_pem": str(key_pem),
        "cert_der": str(cert_der),
        "key_der": str(key_der),
    }

    try:
        # 生成私钥
        subprocess.run(
            ["openssl", "genrsa", "-out", str(key_pem), "2048"],
            check=True, capture_output=True, text=True,
        )

        # 生成自签名证书
        subprocess.run(
            ["openssl", "req", "-new", "-x509",
             "-key", str(key_pem),
             "-out", str(cert_pem),
             "-days", str(days),
             "-subj", subject],
            check=True, capture_output=True, text=True,
        )

        # 导出 DER 格式
        subprocess.run(
            ["openssl", "x509", "-in", str(cert_pem),
             "-outform", "der", "-out", str(cert_der)],
            check=True, capture_output=True, text=True,
        )
        subprocess.run(
            ["openssl", "rsa", "-in", str(key_pem),
             "-outform", "der", "-out", str(key_der)],
            check=True, capture_output=True, text=True,
        )

        print(f"自签名证书已生成:")
        print(f"  证书 (PEM): {cert_pem}")
        print(f"  私钥 (PEM): {key_pem}")
        print(f"  证书 (DER): {cert_der}")
        print(f"  私钥 (DER): {key_der}")
        print(f"  有效期: {days} 天")
        print(f"  CN: {common_name}, O: {org}, C: {country}")

    except FileNotFoundError:
        result["error"] = "未找到 OpenSSL，请先安装: https://www.openssl.org/"
    except subprocess.CalledProcessError as e:
        result["error"] = f"OpenSSL 执行失败: {e.stderr}"
    except Exception as e:
        result["error"] = str(e)

    return result


# ============================================================
# 5. 变量快速读取
# ============================================================

async def read_variable(url: str, node_id: str) -> dict:
    """
    读取单个 OPC UA 变量的值和元数据

    Args:
        url: 服务器端点 URL
        node_id: NodeId 字符串，如 "ns=0;i=2258" 或 "ns=3;s=Temperature"

    Returns:
        {"node_id": str, "value": any, "type": str, "status": str}
    """
    try:
        from asyncua import Client
    except ImportError:
        return {"error": "请先安装 opcua-asyncio: pip install opcua-asyncio"}

    result = {"node_id": node_id}

    try:
        async with Client(url=url, timeout=5) as client:
            node = client.get_node(node_id)
            val = await node.read_value()
            dtype = await node.read_data_type_as_variant_type()
            browse_name = (await node.read_browse_name()).Name

            result["value"] = val
            result["type"] = str(dtype)
            result["browse_name"] = browse_name
            result["status"] = "OK"

            print(f"节点: {browse_name}")
            print(f"NodeId: {node_id}")
            print(f"类型: {dtype}")
            print(f"值: {val}")

    except Exception as e:
        result["status"] = "ERROR"
        result["error"] = str(e)
        print(f"读取失败: {e}")

    return result


# ============================================================
# 6. 健康检查
# ============================================================

async def health_check(url: str) -> dict:
    """
    OPC UA 服务器健康检查

    检查项：端口可达性 → 连接握手 → 会话创建 → 服务器状态读取

    Args:
        url: 服务器端点 URL

    Returns:
        健康检查报告字典
    """
    report = {
        "url": url,
        "timestamp": datetime.now().isoformat(),
        "checks": {},
        "overall": "UNKNOWN",
    }

    # 检查 1：端口可达性
    host = url.replace("opc.tcp://", "").split(":")[0].split("/")[0]
    port = 4840
    if ":" in url.replace("opc.tcp://", "").split("/")[0]:
        port_str = url.replace("opc.tcp://", "").split("/")[0].split(":")[1]
        try:
            port = int(port_str)
        except ValueError:
            pass

    port_check = check_port(host, port)
    report["checks"]["port_reachable"] = port_check

    if not port_check["reachable"]:
        report["overall"] = "DOWN"
        report["summary"] = f"端口 {host}:{port} 不可达"
        return report

    # 检查 2：OPC UA 连接
    try:
        from asyncua import Client
    except ImportError:
        report["checks"]["connection"] = {"error": "opcua-asyncio 未安装"}
        report["overall"] = "UNKNOWN"
        return report

    try:
        async with Client(url=url, timeout=5) as client:
            report["checks"]["connection"] = {"status": "OK", "server_name": ""}

            # 检查 3：服务器状态
            try:
                server_node = client.get_node("ns=0;i=2256")  # ServerStatus
                state_node = client.get_node("ns=0;i=2259")    # State
                state = await state_node.read_value()
                report["checks"]["server_state"] = {"status": "OK", "state": state}
                report["overall"] = "HEALTHY"
                report["summary"] = f"服务器运行正常，状态: {state}"
            except Exception as e:
                report["checks"]["server_state"] = {"status": "WARN", "error": str(e)}
                report["overall"] = "DEGRADED"
                report["summary"] = "连接成功但无法读取服务器状态"

    except Exception as e:
        report["checks"]["connection"] = {"status": "ERROR", "error": str(e)}
        report["overall"] = "DOWN"
        report["summary"] = f"OPC UA 连接失败: {e}"

    return report


# ============================================================
# CLI 入口
# ============================================================

def print_usage():
    print("""
OPC UA 实用工具集

用法:
  python opc_utils.py check <host> [port]       — 检查端口可达性
  python opc_utils.py browse <url> [depth]       — 浏览地址空间
  python opc_utils.py read <url> <node_id>       — 读取变量值
  python opc_utils.py cert [cn] [org]            — 生成自签名证书
  python opc_utils.py health <url>               — 健康检查
  python opc_utils.py discover <url>             — 发现服务器端点

示例:
  python opc_utils.py check 192.168.1.100
  python opc_utils.py browse opc.tcp://127.0.0.1:53530/OPCUA/SimulationServer 2
  python opc_utils.py read opc.tcp://127.0.0.1:4840 "ns=0;i=2258"
  python opc_utils.py cert MyClient MyCompany
  python opc_utils.py health opc.tcp://127.0.0.1:4840
""")


def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    cmd = sys.argv[1]

    if cmd == "check":
        host = sys.argv[2] if len(sys.argv) > 2 else "127.0.0.1"
        port = int(sys.argv[3]) if len(sys.argv) > 3 else 4840
        result = check_port(host, port)
        print(f"\n检查结果: {'可达 ✅' if result['reachable'] else '不可达 ❌'}")
        if result["error"]:
            print(f"错误: {result['error']}")

    elif cmd == "browse":
        if len(sys.argv) < 3:
            print("用法: python opc_utils.py browse <url> [depth]")
            return
        url = sys.argv[2]
        depth = int(sys.argv[3]) if len(sys.argv) > 3 else 3
        asyncio.run(browse_address_space(url, max_depth=depth, show_values=True))

    elif cmd == "read":
        if len(sys.argv) < 4:
            print("用法: python opc_utils.py read <url> <node_id>")
            return
        url = sys.argv[2]
        node_id = sys.argv[3]
        asyncio.run(read_variable(url, node_id))

    elif cmd == "cert":
        cn = sys.argv[2] if len(sys.argv) > 2 else "MyOPCApp"
        org = sys.argv[3] if len(sys.argv) > 3 else "MyCompany"
        generate_self_signed_cert(output_dir="./certs", common_name=cn, org=org)

    elif cmd == "health":
        if len(sys.argv) < 3:
            print("用法: python opc_utils.py health <url>")
            return
        url = sys.argv[2]
        report = asyncio.run(health_check(url))
        print(f"\n健康检查报告:")
        print(f"  目标: {report['url']}")
        print(f"  时间: {report['timestamp']}")
        print(f"  状态: {report['overall']}")
        print(f"  摘要: {report.get('summary', 'N/A')}")
        for check_name, check_data in report["checks"].items():
            status = check_data.get("status", str(check_data))
            print(f"  [{check_name}]: {status}")

    elif cmd == "discover":
        if len(sys.argv) < 3:
            print("用法: python opc_utils.py discover <url>")
            return
        url = sys.argv[2]
        endpoints = asyncio.run(discover_endpoints(url))
        for ep in endpoints:
            print(f"  端点: {ep.get('endpoint_url', 'N/A')}")

    else:
        print(f"未知命令: {cmd}")
        print_usage()


if __name__ == "__main__":
    main()
