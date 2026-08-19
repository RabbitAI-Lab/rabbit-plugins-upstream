"""
alist API 全功能客户端
支持：认证、文件系统、存储管理、用户管理、元信息、设置、任务管理
用法：
  python alist_client.py --base-url http://localhost:80 --username admin --password xxx list /path
  python alist_client.py --base-url http://localhost:80 --api-key xxx list /path
  或通过环境变量：ALIST_BASE_URL, ALIST_USERNAME, ALIST_PASSWORD, ALIST_API_KEY
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Optional

DEFAULT_BASE_URL = "http://localhost:80"
TOKEN_CACHE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".alist_token_cache.json")


class AlistClient:
    """alist REST API 客户端"""

    def __init__(
        self,
        base_url: str = DEFAULT_BASE_URL,
        username: str = "",
        password: str = "",
        api_key: str = "",
        timeout: int = 30,
        retries: int = 2,
    ):
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.password = password
        self.api_key = api_key
        self.timeout = timeout
        self.retries = retries
        self._token: Optional[str] = None
        self._token_expiry: float = 0.0

    # ─── 内部工具 ────────────────────────────────────────────

    def _make_request(self, method: str, path: str, data: Any = None, params: dict = None) -> dict:
        """发送 HTTP 请求，自动带 token"""
        url = f"{self.base_url}{path}"
        headers = {"Content-Type": "application/json"}

        if self.api_key:
            headers["Authorization"] = self.api_key
        else:
            token = self._get_token()
            if token:
                headers["Authorization"] = token

        body = None
        if data is not None:
            body = json.dumps(data).encode("utf-8")

        if params:
            qs = urllib.parse.urlencode(params)
            url = f"{url}?{qs}"

        last_error = None
        for attempt in range(self.retries + 1):
            try:
                req = urllib.request.Request(url, data=body, headers=headers, method=method)
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    raw = resp.read().decode("utf-8")
                    if not raw:
                        return {"code": 200, "message": "success"}
                    return json.loads(raw)
            except urllib.error.HTTPError as e:
                last_error = e
                if e.code == 401 and attempt < self.retries:
                    self._token = None
                    token = self._get_token()
                    if token:
                        headers["Authorization"] = token
                        continue
                err_body = ""
                try:
                    err_body = e.read().decode("utf-8", errors="replace")[:1000]
                except Exception:
                    pass
                return {"code": e.code, "message": str(e), "data": err_body}
            except Exception as e:
                last_error = e
                if attempt < self.retries:
                    time.sleep(1)
                    continue
        return {"code": -1, "message": str(last_error)}

    def _get_token(self) -> str:
        """获取或刷新 token"""
        if self._token and time.time() < self._token_expiry - 60:
            return self._token

        # 尝试从缓存恢复
        cached = self._load_token_cache()
        if (
            cached
            and cached.get("base_url") == self.base_url
            and cached.get("username") == self.username
            and cached.get("token")
            and time.time() < cached.get("expiry", 0) - 60
        ):
            self._token = cached["token"]
            self._token_expiry = cached["expiry"]
            return self._token

        # 登录
        if not self.username or not self.password:
            return ""

        result = self._raw_login()
        if result.get("code") == 200:
            token = result["data"]["token"]
            self._token = token
            self._token_expiry = time.time() + 48 * 3600  # alist token 默认 48h
            self._save_token_cache()
            return token
        return ""

    def _raw_login(self) -> dict:
        """原始登录请求（不触发 token 重试）"""
        import hashlib

        url = f"{self.base_url}/api/auth/login/hash"
        headers = {"Content-Type": "application/json"}

        # 先获取 salt
        body = json.dumps({"username": self.username, "password": "", "otp_code": ""}).encode("utf-8")
        try:
            req = urllib.request.Request(url, data=body, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                pass  # 请求只用来触发 salt 返回，实际 alist 新版本在响应头中
        except urllib.error.HTTPError as e:
            if e.code != 400:
                return {"code": e.code, "message": str(e)}

        # 直接尝试密码哈希登录
        hashed = hashlib.sha256(
            (self.password + "-" + hashlib.sha256(self.password.encode()).hexdigest()).encode()
        ).hexdigest()
        body = json.dumps({"username": self.username, "password": hashed, "otp_code": ""}).encode("utf-8")
        req = urllib.request.Request(url, data=body, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def _load_token_cache(self) -> dict:
        try:
            with open(TOKEN_CACHE_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {}

    def _save_token_cache(self):
        try:
            with open(TOKEN_CACHE_FILE, "w") as f:
                json.dump({
                    "base_url": self.base_url,
                    "username": self.username,
                    "token": self._token,
                    "expiry": self._token_expiry,
                }, f)
        except Exception:
            pass

    # ─── 认证 ────────────────────────────────────────────────

    def login(self) -> dict:
        """登录并缓存 token"""
        self._token = None
        token = self._get_token()
        if token:
            return {"code": 200, "message": "登录成功", "token": token}
        return {"code": -1, "message": "登录失败，请检查用户名密码"}

    # ─── 文件系统操作 ─────────────────────────────────────────

    def list_files(
        self, path: str = "/", password: str = "", page: int = 1, per_page: int = 0, refresh: bool = False
    ) -> dict:
        """列出目录内容"""
        data = {"path": path, "password": password, "page": page, "per_page": per_page, "refresh": refresh}
        return self._make_request("POST", "/api/fs/list", data)

    def get_file(self, path: str, password: str = "") -> dict:
        """获取文件/目录详细信息"""
        data = {"path": path, "password": password}
        return self._make_request("POST", "/api/fs/get", data)

    def search_files(self, keyword: str, scope: int = 0, page: int = 1, per_page: int = 100) -> dict:
        """搜索文件（scope: 0=全部, 1=当前目录, 2=子目录）"""
        data = {"keywords": keyword, "scope": scope, "page": page, "per_page": per_page}
        return self._make_request("POST", "/api/fs/search", data)

    def mkdir(self, path: str) -> dict:
        """创建目录"""
        return self._make_request("POST", "/api/fs/mkdir", {"path": path})

    def rename(self, path: str, name: str) -> dict:
        """重命名文件或目录（name 为新名称，不含路径）"""
        return self._make_request("POST", "/api/fs/rename", {"path": path, "name": name})

    def move(self, src_dir: str, dst_dir: str, names: list[str], timeout: int = None, verify: bool = True) -> dict:
        """移动文件。timeout 覆盖默认超时，跨存储大文件建议设 3600+。
        verify=True 时调用后查询 alist 任务列表确认所有 copy 任务完成（跨盘时文件预占空间，禁止用文件大小/存在性判断）。"""
        old_timeout = self.timeout
        if timeout:
            self.timeout = timeout
        try:
            result = self._make_request("POST", "/api/fs/move", {"src_dir": src_dir, "dst_dir": dst_dir, "names": names})
        finally:
            self.timeout = old_timeout

        if verify and result.get("code") == 200:
            return self._verify_by_tasks(names, result)
        return result

    def _verify_by_tasks(self, names: list[str], result: dict) -> dict:
        """以 alist 任务列表状态为唯一判断标准。
        不论是同存储还是跨存储，alist 都会在 task_copy_list 生成任务记录，status=4 表示完成。
        验证通过后自动删除已完成任务，避免任务列表堆积。"""
        tasks_resp = self.task_copy_list()
        if tasks_resp.get("code") != 200:
            result["_verify_warning"] = "无法获取任务列表"
            return result

        all_tasks = tasks_resp.get("data", {}).get("tasks", []) or []
        name_set = set(names)
        matched = [t for t in all_tasks if t.get("name") in name_set]

        if not matched:
            # 同名任务尚未生成（刚提交，alist 还未写入任务记录）
            result["_unmatched"] = list(name_set)
            result["_verified"] = f"task_list: no matching tasks yet for {len(name_set)} file(s), retry needed"
            return result

        succeeded = [t for t in matched if t.get("status") == 4]
        errors = [t for t in matched if t.get("status") == 3]
        running = [t for t in matched if t.get("status") in (0, 1, 2)]

        if errors:
            result["code"] = -2
            result["message"] = f"任务列表有 {len(errors)} 项失败"
            result["_failed_tasks"] = [
                {"tid": t.get("tid"), "name": t.get("name"), "status": t.get("status"),
                 "error": t.get("error", "")} for t in errors
            ]
        if running:
            result["_running_tasks"] = [
                {"tid": t.get("tid"), "name": t.get("name"), "status": t.get("status")} for t in running
            ]

        # 验证通过（全部 status=4）：清理已完成任务
        if not errors and not running:
            cleaned = 0
            for t in succeeded:
                tid = t.get("tid")
                if tid:
                    try:
                        self.task_delete(tid, "copy")
                        cleaned += 1
                    except Exception:
                        pass
            result["_verified"] = f"task_list: all {len(succeeded)} tasks succeeded, {cleaned} cleaned"

        return result

    def recursive_move(self, src_dir: str, dst_dir: str, verify: bool = True) -> dict:
        """递归移动整个目录树。verify=True 时调用后检查任务列表，验证通过自动清理已完成任务。"""
        result = self._make_request("POST", "/api/fs/recursive_move", {"src_dir": src_dir, "dst_dir": dst_dir})
        if verify and result.get("code") == 200:
            tasks_resp = self.task_copy_list()
            if tasks_resp.get("code") == 200:
                all_tasks = tasks_resp.get("data", {}).get("tasks", []) or []
                running = [t for t in all_tasks if t.get("status") in (0, 1, 2)]
                errors = [t for t in all_tasks if t.get("status") == 3]
                succeeded = [t for t in all_tasks if t.get("status") == 4]
                if errors:
                    result["code"] = -2
                    result["message"] = f"recursive_move 任务列表有 {len(errors)} 项失败"
                    result["_failed_tasks"] = [
                        {"tid": t.get("tid"), "name": t.get("name"), "error": t.get("error", "")} for t in errors
                    ]
                if running:
                    result["_running_tasks"] = [
                        {"tid": t.get("tid"), "name": t.get("name"), "status": t.get("status")} for t in running
                    ]
                # 清理已完成任务
                if not errors and not running:
                    cleaned = 0
                    for t in succeeded:
                        tid = t.get("tid")
                        if tid:
                            try:
                                self.task_delete(tid, "copy")
                                cleaned += 1
                            except Exception:
                                pass
                    result["_verified"] = f"recursive_move: all {len(succeeded)} tasks succeeded, {cleaned} cleaned"
        return result

    def copy(self, src_dir: str, dst_dir: str, names: list[str], verify: bool = True) -> dict:
        """复制文件。verify=True 时调用后查询 alist 任务列表确认复制完成。"""
        result = self._make_request("POST", "/api/fs/copy", {"src_dir": src_dir, "dst_dir": dst_dir, "names": names})
        if verify and result.get("code") == 200:
            return self._verify_by_tasks(names, result)
        return result

    def remove(self, dir_path: str, names: list[str]) -> dict:
        """删除文件/目录"""
        return self._make_request("POST", "/api/fs/remove", {"dir": dir_path, "names": names})

    def dirs(self, path: str = "/", password: str = "", force_root: bool = False) -> dict:
        """获取子目录列表（含文件/目录计数，刮削前置扫描用）"""
        data = {"path": path, "password": password}
        if force_root:
            data["force_root"] = True
        return self._make_request("POST", "/api/fs/dirs", data)

    def add_offline_download(self, urls: list[str], save_path: str, tool: str = "aria2") -> dict:
        """添加离线下载任务（aria2 / qBittorrent）。

        参数:
            urls: 下载链接列表
            save_path: alist 保存目录
            tool: 下载工具，默认 aria2
        """
        data = {"path": save_path, "urls": urls, "tool": tool}
        return self._make_request("POST", "/api/fs/add_offline_download", data)

    def add_aria2(self, urls: list[str], save_path: str) -> dict:
        """添加 aria2 下载任务（简化版 offline download）"""
        data = {"path": save_path, "urls": urls}
        return self._make_request("POST", "/api/fs/add_aria2", data)

    def upload_file(self, local_file_path: str, remote_dir: str, timeout: int = None, verify: bool = True) -> dict:
        """上传文件到 alist。使用 alist 内置 PUT /api/fs/form 端点上传统一流。
        verify=True 时调用后查询 task_upload_list 确认所有上传任务完成并自动清理。

        参数:
            local_file_path: 本地文件绝对路径
            remote_dir: alist 目标目录路径，如 /storage/movies/
            timeout: 覆盖默认超时（大文件建议 3600+）
            verify: 是否事后验证任务列表
        """
        local_path = Path(local_file_path)
        if not local_path.is_file():
            return {"code": -1, "message": f"本地文件不存在: {local_file_path}"}

        file_name = local_path.name
        remote_path = f"{remote_dir.rstrip('/')}/{file_name}"

        old_timeout = self.timeout
        if timeout:
            self.timeout = timeout
        try:
            url = f"{self.base_url}/api/fs/form"
            boundary = f"alist-upload-{int(time.time() * 1000)}"
            headers = {
                "Content-Type": f"multipart/form-data; boundary={boundary}",
                "File-Path": remote_path,
            }
            if self.api_key:
                headers["Authorization"] = self.api_key
            else:
                token = self._get_token()
                if token:
                    headers["Authorization"] = token

            # multipart 构造文件字段
            file_bytes = local_path.read_bytes()
            body = (
                f"--{boundary}\r\n"
                f'Content-Disposition: form-data; name="file"; filename="{file_name}"\r\n'
                f"Content-Type: application/octet-stream\r\n"
                f"\r\n"
            ).encode("utf-8") + file_bytes + f"\r\n--{boundary}--\r\n".encode("utf-8")

            last_error = None
            for attempt in range(self.retries + 1):
                try:
                    req = urllib.request.Request(url, data=body, headers=headers, method="PUT")
                    with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                        raw = resp.read().decode("utf-8")
                        result = json.loads(raw) if raw else {"code": 200, "message": "success"}
                        break
                except urllib.error.HTTPError as e:
                    last_error = e
                    if e.code == 401 and attempt < self.retries:
                        self._token = None
                        token = self._get_token()
                        if token:
                            headers["Authorization"] = token
                            continue
                    err_body = ""
                    try:
                        err_body = e.read().decode("utf-8", errors="replace")[:1000]
                    except Exception:
                        pass
                    result = {"code": e.code, "message": str(e), "data": err_body}
                    break
                except Exception as e:
                    last_error = e
                    if attempt < self.retries:
                        time.sleep(1)
                        continue
                    result = {"code": -1, "message": str(last_error)}
                    break
        finally:
            self.timeout = old_timeout

        if verify and result.get("code") == 200:
            return self._verify_upload_tasks([file_name], result)
        return result

    def download_file(self, remote_path: str, local_dir: str, timeout: int = None, verify: bool = True) -> dict:
        """从 alist 下载文件到本地。使用 alist 内置 raw 端点上传统一下载。
        verify=True 时调用后查询 task_download_list 确认下载任务完成并自动清理。

        参数:
            remote_path: alist 文件路径，如 /storage/movies/video.mp4
            local_dir: 本地目标目录
            timeout: 覆盖默认超时（大文件建议 3600+）
            verify: 是否事后验证任务列表
        """
        remote_path = remote_path.lstrip("/")
        file_name = remote_path.split("/")[-1]
        local_path = os.path.join(local_dir, file_name)

        old_timeout = self.timeout
        if timeout:
            self.timeout = timeout
        try:
            url = f"{self.base_url}/d/{remote_path}"
            headers = {}
            if self.api_key:
                headers["Authorization"] = self.api_key
            else:
                token = self._get_token()
                if token:
                    headers["Authorization"] = token

            last_error = None
            for attempt in range(self.retries + 1):
                try:
                    req = urllib.request.Request(url, headers=headers, method="GET")
                    with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                        os.makedirs(local_dir, exist_ok=True)
                        with open(local_path, "wb") as f:
                            while True:
                                chunk = resp.read(8192)
                                if not chunk:
                                    break
                                f.write(chunk)
                    file_size = os.path.getsize(local_path)
                    result = {"code": 200, "message": "success", "data": {"local_path": local_path, "size": file_size}}
                    break
                except urllib.error.HTTPError as e:
                    last_error = e
                    if e.code == 401 and attempt < self.retries:
                        self._token = None
                        token = self._get_token()
                        if token:
                            headers["Authorization"] = token
                            continue
                    err_body = ""
                    try:
                        err_body = e.read().decode("utf-8", errors="replace")[:1000]
                    except Exception:
                        pass
                    result = {"code": e.code, "message": str(e), "data": err_body}
                    break
                except Exception as e:
                    last_error = e
                    if attempt < self.retries:
                        time.sleep(1)
                        continue
                    result = {"code": -1, "message": str(last_error)}
                    break
        finally:
            self.timeout = old_timeout

        if verify and result.get("code") == 200:
            return self._verify_download_tasks([file_name], result)
        return result

    def _verify_upload_tasks(self, file_names: list[str], result: dict) -> dict:
        """以 task_upload_list 状态为唯一判断标准（与 _verify_by_tasks 模式一致）。
        status=4 表示上传完成，验证通过后自动清理已完成任务。"""
        tasks_resp = self.task_upload_list()
        if tasks_resp.get("code") != 200:
            result["_verify_warning"] = "无法获取上传任务列表"
            return result

        all_tasks = tasks_resp.get("data", {}).get("tasks", []) or []
        name_set = set(file_names)
        matched = [t for t in all_tasks if t.get("name") in name_set]

        if not matched:
            result["_unmatched"] = list(name_set)
            result["_verified"] = f"task_upload_list: no matching tasks yet for {len(file_names)} file(s), retry needed"
            return result

        succeeded = [t for t in matched if t.get("status") == 4]
        errors = [t for t in matched if t.get("status") == 3]
        running = [t for t in matched if t.get("status") in (0, 1, 2)]

        if errors:
            result["code"] = -2
            result["message"] = f"上传任务列表有 {len(errors)} 项失败"
            result["_failed_tasks"] = [
                {"tid": t.get("tid"), "name": t.get("name"), "status": t.get("status"),
                 "error": t.get("error", "")} for t in errors
            ]
        if running:
            result["_running_tasks"] = [
                {"tid": t.get("tid"), "name": t.get("name"), "status": t.get("status")} for t in running
            ]

        if not errors and not running:
            cleaned = 0
            for t in succeeded:
                tid = t.get("tid")
                if tid:
                    try:
                        self.task_delete(tid, "upload")
                        cleaned += 1
                    except Exception:
                        pass
            result["_verified"] = f"task_upload_list: all {len(succeeded)} tasks succeeded, {cleaned} cleaned"

        return result

    def _verify_download_tasks(self, file_names: list[str], result: dict) -> dict:
        """以 task_download_list 状态为唯一判断标准（与 _verify_by_tasks 模式一致）。
        status=4 表示下载完成，验证通过后自动清理已完成任务。"""
        tasks_resp = self.task_download_list()
        if tasks_resp.get("code") != 200:
            result["_verify_warning"] = "无法获取下载任务列表"
            return result

        all_tasks = tasks_resp.get("data", {}).get("tasks", []) or []
        name_set = set(file_names)
        matched = [t for t in all_tasks if t.get("name") in name_set]

        if not matched:
            result["_unmatched"] = list(name_set)
            result["_verified"] = f"task_download_list: no matching tasks yet for {len(file_names)} file(s), retry needed"
            return result

        succeeded = [t for t in matched if t.get("status") == 4]
        errors = [t for t in matched if t.get("status") == 3]
        running = [t for t in matched if t.get("status") in (0, 1, 2)]

        if errors:
            result["code"] = -2
            result["message"] = f"下载任务列表有 {len(errors)} 项失败"
            result["_failed_tasks"] = [
                {"tid": t.get("tid"), "name": t.get("name"), "status": t.get("status"),
                 "error": t.get("error", "")} for t in errors
            ]
        if running:
            result["_running_tasks"] = [
                {"tid": t.get("tid"), "name": t.get("name"), "status": t.get("status")} for t in running
            ]

        if not errors and not running:
            cleaned = 0
            for t in succeeded:
                tid = t.get("tid")
                if tid:
                    try:
                        self.task_delete(tid, "download")
                        cleaned += 1
                    except Exception:
                        pass
            result["_verified"] = f"task_download_list: all {len(succeeded)} tasks succeeded, {cleaned} cleaned"

        return result

    # ─── 存储管理 ────────────────────────────────────────────

    def storage_list(self, page: int = 1, per_page: int = 100) -> dict:
        """获取所有存储列表"""
        return self._make_request("GET", "/api/admin/storage/list", params={"page": page, "per_page": per_page})

    def storage_get(self, id: int) -> dict:
        """获取指定存储信息"""
        return self._make_request("GET", "/api/admin/storage/get", params={"id": id})

    def storage_create(self, mount_path: str, driver: str, addition: dict) -> dict:
        """创建存储"""
        data = {"mount_path": mount_path, "driver": driver, "addition": json.dumps(addition)}
        return self._make_request("POST", "/api/admin/storage/create", data)

    def storage_update(self, id: int, mount_path: str, driver: str, addition: dict) -> dict:
        """更新存储配置"""
        data = {"id": id, "mount_path": mount_path, "driver": driver, "addition": json.dumps(addition)}
        return self._make_request("POST", "/api/admin/storage/update", data)

    def storage_delete(self, id: int) -> dict:
        """删除存储"""
        return self._make_request("POST", "/api/admin/storage/delete", {"id": id})

    def storage_enable(self, id: int) -> dict:
        """启用存储"""
        return self._make_request("POST", "/api/admin/storage/enable", {"id": id})

    def storage_disable(self, id: int) -> dict:
        """禁用存储"""
        return self._make_request("POST", "/api/admin/storage/disable", {"id": id})

    def storage_refresh(self) -> dict:
        """刷新所有存储缓存"""
        return self._make_request("POST", "/api/admin/storage/refresh")

    def driver_list(self) -> dict:
        """获取所有驱动配置模板"""
        return self._make_request("GET", "/api/admin/driver/list")

    def driver_names(self) -> dict:
        """获取所有驱动名称"""
        return self._make_request("GET", "/api/admin/driver/names")

    def driver_info(self, driver: str) -> dict:
        """获取指定驱动的配置字段定义"""
        return self._make_request("POST", "/api/admin/driver/info", {"driver": driver})

    # ─── 用户管理 ────────────────────────────────────────────

    def user_list(self, page: int = 1, per_page: int = 100) -> dict:
        """获取用户列表"""
        return self._make_request("GET", "/api/admin/user/list", params={"page": page, "per_page": per_page})

    def user_get(self, id: int) -> dict:
        """获取指定用户信息"""
        return self._make_request("GET", "/api/admin/user/get", params={"id": id})

    def user_create(self, username: str, password: str, base_path: str = "/",
                    role: int = 2, permission: int = 0, disabled: bool = False) -> dict:
        """创建用户（role: 0=admin, 1=guest, 2=user）"""
        data = {
            "username": username, "password": password, "base_path": base_path,
            "role": role, "permission": permission, "disabled": disabled,
        }
        return self._make_request("POST", "/api/admin/user/create", data)

    def user_update(self, id: int, **kwargs) -> dict:
        """更新用户信息"""
        data = {"id": id, **kwargs}
        return self._make_request("POST", "/api/admin/user/update", data)

    def user_delete(self, id: int) -> dict:
        """删除用户"""
        return self._make_request("POST", "/api/admin/user/delete", {"id": id})

    # ─── 元信息管理 ──────────────────────────────────────────

    def meta_list(self, page: int = 1, per_page: int = 100) -> dict:
        """获取元信息列表"""
        return self._make_request("GET", "/api/admin/meta/list", params={"page": page, "per_page": per_page})

    def meta_create(self, path: str, key: str, value: str) -> dict:
        """创建元信息"""
        return self._make_request("POST", "/api/admin/meta/create", {"path": path, "key": key, "value": value})

    def meta_update(self, id: int, path: str, key: str, value: str) -> dict:
        """更新元信息"""
        return self._make_request("POST", "/api/admin/meta/update", {"id": id, "path": path, "key": key, "value": value})

    def meta_delete(self, id: int) -> dict:
        """删除元信息"""
        return self._make_request("POST", "/api/admin/meta/delete", {"id": id})

    # ─── 设置管理 ────────────────────────────────────────────

    def setting_list(self, groups: list[int] = None, keys: list[str] = None) -> dict:
        """获取设置列表（groups: 0=public,1=site,2=style,...）"""
        data = {}
        if groups:
            data["groups"] = groups
        if keys:
            data["keys"] = keys
        return self._make_request("GET", "/api/admin/setting/list", data) if data else self._make_request("GET", "/api/admin/setting/list")

    def setting_get(self, key: str) -> dict:
        """获取单个设置项"""
        return self._make_request("GET", "/api/admin/setting/get", params={"key": key})

    def setting_save(self, items: list[dict]) -> dict:
        """批量保存设置（items: [{"key":"xxx","value":"yyy"},...]）"""
        return self._make_request("POST", "/api/admin/setting/save", items)

    def setting_delete(self, key: str) -> dict:
        """删除设置项"""
        return self._make_request("POST", "/api/admin/setting/delete", {"key": key})

    def setting_reset(self) -> dict:
        """重置所有设置"""
        return self._make_request("POST", "/api/admin/setting/reset")

    # ─── 任务管理 ────────────────────────────────────────────

    def task_upload_list(self) -> dict:
        """上传任务列表"""
        return self._make_request("GET", "/api/admin/task/upload")

    def task_download_list(self) -> dict:
        """下载任务列表"""
        return self._make_request("GET", "/api/admin/task/download")

    def task_copy_list(self) -> dict:
        """复制任务列表"""
        return self._make_request("GET", "/api/admin/task/copy")

    def task_delete(self, tid: str, task_type: str) -> dict:
        """删除任务（task_type: upload/download/copy）"""
        return self._make_request("POST", "/api/admin/task/delete", {"tid": tid, "type": task_type})

    def task_cancel(self, tid: str, task_type: str) -> dict:
        """取消任务"""
        return self._make_request("POST", "/api/admin/task/cancel", {"tid": tid, "type": task_type})

    def task_retry(self, tid: str, task_type: str) -> dict:
        """重试失败任务"""
        return self._make_request("POST", "/api/admin/task/retry", {"tid": tid, "type": task_type})

    def task_clear_done(self) -> dict:
        """清除已完成任务"""
        return self._make_request("POST", "/api/admin/task/clear_done")

    def task_clear_succeeded(self) -> dict:
        """清除已成功任务"""
        return self._make_request("POST", "/api/admin/task/clear_succeeded")

    def task_clear(self) -> dict:
        """清除全部任务"""
        return self._make_request("POST", "/api/admin/task/clear")

    # ─── 索引管理 ────────────────────────────────────────────

    def index_build(self, paths: list[str], max_depth: int = 20, count: int = 0) -> dict:
        """构建索引"""
        data = {"paths": paths, "max_depth": max_depth, "count": count}
        return self._make_request("POST", "/api/admin/index/build", data)

    def index_update(self, paths: list[str]) -> dict:
        """更新索引"""
        return self._make_request("POST", "/api/admin/index/update", {"paths": paths})

    def index_stop(self) -> dict:
        """停止索引"""
        return self._make_request("POST", "/api/admin/index/stop")

    def index_clear(self) -> dict:
        """清除索引"""
        return self._make_request("POST", "/api/admin/index/clear")

    def index_progress(self) -> dict:
        """索引进度"""
        return self._make_request("GET", "/api/admin/index/progress")

    # ─── 备份恢复 ────────────────────────────────────────────

    def backup_list(self) -> dict:
        """备份列表"""
        return self._make_request("GET", "/api/admin/backup/list")

    def backup_backup(self) -> dict:
        """创建备份"""
        return self._make_request("POST", "/api/admin/backup/backup")

    def backup_restore(self, filename: str) -> dict:
        """恢复备份"""
        return self._make_request("POST", "/api/admin/backup/restore", {"filename": filename})

    def backup_delete(self, filename: str) -> dict:
        """删除备份"""
        return self._make_request("POST", "/api/admin/backup/delete", {"filename": filename})

    # ─── SSH/SFTP ─────────────────────────────────────────────

    def ssh_list(self) -> dict:
        """列出 SSH 连接"""
        return self._make_request("GET", "/api/admin/ssh/list")

    def ssh_create(self, host: str, port: int = 22, username: str = "root",
                   password: str = "", private_key: str = "") -> dict:
        """创建 SSH 连接"""
        data = {"host": host, "port": port, "username": username}
        if password:
            data["password"] = password
        if private_key:
            data["private_key"] = private_key
        return self._make_request("POST", "/api/admin/ssh/create", data)

    def ssh_update(self, id: int, **kwargs) -> dict:
        """更新 SSH 连接"""
        data = {"id": id, **kwargs}
        return self._make_request("POST", "/api/admin/ssh/update", data)

    def ssh_delete(self, id: int) -> dict:
        """删除 SSH 连接"""
        return self._make_request("POST", "/api/admin/ssh/delete", {"id": id})

    # ─── 审计日志 ────────────────────────────────────────────

    def audit_list(self, page: int = 1, per_page: int = 100) -> dict:
        """审计日志列表"""
        return self._make_request("GET", "/api/admin/audit/list", params={"page": page, "per_page": per_page})

    def audit_clear(self) -> dict:
        """清除审计日志"""
        return self._make_request("POST", "/api/admin/audit/clear")

    # ─── 公告 ────────────────────────────────────────────────

    def announcement_list(self) -> dict:
        """公告列表"""
        return self._make_request("GET", "/api/admin/announcement/list")

    def announcement_update(self, content: str, show_expiration: int = 0) -> dict:
        """更新公告"""
        data = {"content": content, "show_expiration": show_expiration}
        return self._make_request("POST", "/api/admin/announcement/update", data)

    # ─── 2FA ─────────────────────────────────────────────────

    def twofa_list(self) -> dict:
        """获取 2FA 配置列表（仅 admin 可用）"""
        return self._make_request("GET", "/api/admin/2fa/list")

    def twofa_delete(self, id: int) -> dict:
        """删除指定用户的 2FA 配置"""
        return self._make_request("POST", "/api/admin/2fa/delete", {"id": id})

    # ─── SSO ─────────────────────────────────────────────────

    def sso_list(self) -> dict:
        """列出 SSO 提供商"""
        return self._make_request("GET", "/api/admin/sso/list")

    def sso_create(self, sso_type: str, name: str, config: dict) -> dict:
        """创建 SSO 提供商"""
        data = {"type": sso_type, "name": name, "config": config}
        return self._make_request("POST", "/api/admin/sso/create", data)

    def sso_update(self, id: int, **kwargs) -> dict:
        """更新 SSO 提供商"""
        data = {"id": id, **kwargs}
        return self._make_request("POST", "/api/admin/sso/update", data)

    def sso_delete(self, id: int) -> dict:
        """删除 SSO 提供商"""
        return self._make_request("POST", "/api/admin/sso/delete", {"id": id})

    # ─── 便捷方法 ────────────────────────────────────────────

    def ping(self) -> dict:
        """测试连接"""
        try:
            return self._make_request("GET", "/api/public/settings")
        except Exception as e:
            return {"code": -1, "message": str(e)}

    def tree(self, path: str = "/", depth: int = 2) -> str:
        """以树形结构展示目录"""
        result = self.list_files(path, per_page=0)
        if result.get("code") != 200:
            return f"Error: {result.get('message')}"

        content = result.get("data", {}).get("content", []) if isinstance(result.get("data"), dict) else []

        def _render(items, indent=0, max_depth=2):
            lines = []
            prefix = "  " * indent
            for item in items:
                name = item.get("name", "")
                is_dir = item.get("is_dir", False)
                size = item.get("size", 0)
                size_str = f" [{size}]" if not is_dir and size else ""
                lines.append(f"{prefix}{'📁' if is_dir else '📄'} {name}{size_str}")
                if is_dir and indent < max_depth:
                    sub = self.list_files(
                        (path.rstrip("/") + "/" + name).replace("//", "/"), per_page=0
                    )
                    subs = sub.get("data", {}).get("content", []) if isinstance(sub.get("data"), dict) else []
                    if subs:
                        for line in _render(subs[:10], indent + 1, max_depth):
                            lines.append(line)
            return lines

        return "\n".join(_render(content[:100], 0, depth))

    def diagnose_scrape(self, path: str) -> dict:
        """刮削诊断：检查目标目录的刮削相关配置、连通性和产物
        
        Returns:
            dict 包含 tmdb_config / connectivity / files / timestamp / verdict
        """
        import time as _time
        result = {
            "tmdb_config": {},
            "connectivity": {},
            "files": [],
            "timestamp": _time.strftime("%Y-%m-%d %H:%M:%S"),
            "verdict": "OK"
        }

        # 1. 检查 TMDB 设置
        try:
            settings = self.setting_list()
            if isinstance(settings, dict) and settings.get("code") == 200:
                data = settings.get("data", {})
                keys = (
                    ["tmdb_api_key", "tmdb_api_url", "http_proxy",
                     "external_previews", "https_proxy"]
                )
                for k in keys:
                    if k in data:
                        val = data[k]
                        # 隐藏 api_key 大部分内容
                        if k == "tmdb_api_key" and isinstance(val, str) and len(val) > 8:
                            val = val[:4] + "****" + val[-4:]
                        result["tmdb_config"][k] = val

                # 检查 tmdb_api_url 是否误设为代理地址
                tmdb_url = data.get("tmdb_api_url", "")
                if isinstance(tmdb_url, str) and tmdb_url.startswith("http://192.168"):
                    result["verdict"] = "MISCONFIGURED"
                    result["tmdb_config"]["_warning"] = (
                        "tmdb_api_url 疑似被设为代理地址而非真实 TMDB API 地址"
                    )
        except Exception as e:
            result["tmdb_config"]["_error"] = str(e)
            result["verdict"] = "ERROR"

        # 2. 测试 TMDB 连通性（通过 alist 后端）
        try:
            # 通过 ping 接口间接测试后端连通性
            ping = self.ping()
            result["connectivity"]["backend"] = "OK" if ping.get("code") == 200 else str(ping)
        except Exception as e:
            result["connectivity"]["backend"] = f"FAIL: {e}"
            if result["verdict"] != "MISCONFIGURED":
                result["verdict"] = "ERROR"

        # 3. 检查目标目录的文件和 NFO 状态
        try:
            fs = self.get_file(path)
            if isinstance(fs, dict) and fs.get("code") == 200:
                data = fs.get("data", {})
                result["files"]["related_info"] = data.get("related_info")
                result["files"]["thumb"] = data.get("thumb", "")
        except Exception as e:
            result["files"]["_get_error"] = str(e)

        # 4. 列出目录下所有文件，检查 NFO/poster 存在性
        try:
            listing = self.list_files(path)
            if isinstance(listing, dict) and listing.get("code") == 200:
                data = listing.get("data", {})
                content = data.get("content", []) if isinstance(data, dict) else []
                nfo_files = []
                poster_files = []
                video_files = []
                for f in content:
                    name = f.get("name", "")
                    if name.lower().endswith(".nfo"):
                        nfo_files.append(name)
                    elif name.lower() in ("poster.jpg", "poster.png", "poster.webp"):
                        poster_files.append(name)
                    elif any(name.lower().endswith(ext) for ext in
                             (".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".m2ts", ".ts")):
                        video_files.append(name)

                result["files"]["nfo_count"] = len(nfo_files)
                result["files"]["poster_count"] = len(poster_files)
                result["files"]["video_count"] = len(video_files)
                if nfo_files:
                    result["files"]["nfo_files"] = nfo_files[:10]
                if poster_files:
                    result["files"]["poster_files"] = poster_files[:10]

                # 5. 综合判定
                if not video_files:
                    result["verdict"] = "NO_MEDIA"
                elif poster_files and not nfo_files:
                    result["verdict"] = "SKIPPED"
                    result["files"]["_note"] = (
                        "存在 poster.jpg 但无 NFO，alist 可能因已有海报跳过刮削。"
                        "重命名 poster.jpg 后重新浏览此目录可触发完整刮削。"
                    )
                elif not poster_files and not nfo_files:
                    result["verdict"] = "NOT_SCRAPED"
        except Exception as e:
            result["files"]["_list_error"] = str(e)

        return result


def main():
    parser = argparse.ArgumentParser(description="alist API 全功能客户端")
    parser.add_argument("--base-url", default=os.getenv("ALIST_BASE_URL", DEFAULT_BASE_URL))
    parser.add_argument("--username", default=os.getenv("ALIST_USERNAME", ""))
    parser.add_argument("--password", default=os.getenv("ALIST_PASSWORD", ""))
    parser.add_argument("--api-key", default=os.getenv("ALIST_API_KEY", ""))
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--output", default="", help="输出 JSON 到文件")

    sub = parser.add_subparsers(dest="action", required=True)

    # 认证
    sub.add_parser("login", help="登录并缓存 token")
    sub.add_parser("ping", help="测试连接")

    # 文件系统
    p = sub.add_parser("list", aliases=["ls"], help="列出目录")
    p.add_argument("path", nargs="?", default="/")
    p.add_argument("--password", default="")
    p.add_argument("--page", type=int, default=1)

    p = sub.add_parser("get", help="获取文件详情")
    p.add_argument("path")
    p.add_argument("--password", default="")

    p = sub.add_parser("search", help="搜索文件")
    p.add_argument("keyword")
    p.add_argument("--scope", type=int, default=0)

    p = sub.add_parser("mkdir", help="创建目录")
    p.add_argument("path")

    p = sub.add_parser("rename", help="重命名")
    p.add_argument("path")
    p.add_argument("name")

    p = sub.add_parser("move", help="移动文件")
    p.add_argument("src_dir")
    p.add_argument("dst_dir")
    p.add_argument("names", nargs="+")

    p = sub.add_parser("recursive-move", help="递归移动")
    p.add_argument("src_dir")
    p.add_argument("dst_dir")

    p = sub.add_parser("copy", help="复制文件")
    p.add_argument("src_dir")
    p.add_argument("dst_dir")
    p.add_argument("names", nargs="+")

    p = sub.add_parser("remove", aliases=["rm"], help="删除文件")
    p.add_argument("dir")
    p.add_argument("names", nargs="+")

    # 文件系统扩展
    p = sub.add_parser("dirs", help="获取子目录列表（刮削前置扫描）")
    p.add_argument("path", nargs="?", default="/")
    p.add_argument("--password", default="")
    p.add_argument("--force-root", action="store_true")

    p = sub.add_parser("offline-download", help="添加离线下载任务")
    p.add_argument("save_path")
    p.add_argument("urls", nargs="+")
    p.add_argument("--tool", default="aria2")

    p = sub.add_parser("add-aria2", help="添加 aria2 下载")
    p.add_argument("save_path")
    p.add_argument("urls", nargs="+")

    p = sub.add_parser("upload", help="上传文件")
    p.add_argument("local_file")
    p.add_argument("remote_dir")

    p = sub.add_parser("download", help="下载文件")
    p.add_argument("remote_path")
    p.add_argument("local_dir")

    # 存储
    sub.add_parser("storage-list", help="存储列表")
    p = sub.add_parser("storage-get", help="获取存储信息")
    p.add_argument("id", type=int)
    sub.add_parser("storage-refresh", help="刷新存储缓存")
    p = sub.add_parser("storage-enable", help="启用存储")
    p.add_argument("id", type=int)
    p = sub.add_parser("storage-disable", help="禁用存储")
    p.add_argument("id", type=int)
    p = sub.add_parser("storage-delete", help="删除存储")
    p.add_argument("id", type=int)

    sub.add_parser("driver-list", help="驱动列表")
    sub.add_parser("driver-names", help="驱动名称")
    p = sub.add_parser("driver-info", help="获取驱动配置字段")
    p.add_argument("driver")

    # 用户
    sub.add_parser("user-list", help="用户列表")
    p = sub.add_parser("user-get", help="获取用户")
    p.add_argument("id", type=int)
    p = sub.add_parser("user-delete", help="删除用户")
    p.add_argument("id", type=int)

    # 任务
    sub.add_parser("task-upload", help="上传任务列表")
    sub.add_parser("task-download", help="下载任务列表")
    sub.add_parser("task-copy", help="复制任务列表")
    sub.add_parser("task-clear-done", help="清除已完成任务")
    sub.add_parser("task-clear-succeeded", help="清除已成功任务")
    sub.add_parser("task-clear", help="清除全部任务")

    # 索引管理
    sub.add_parser("index-progress", help="索引进度")
    sub.add_parser("index-stop", help="停止索引")
    sub.add_parser("index-clear", help="清除索引")

    # 备份恢复
    sub.add_parser("backup-list", help="备份列表")
    sub.add_parser("backup-backup", help="创建备份")

    # SSH
    sub.add_parser("ssh-list", help="SSH 连接列表")

    # 审计
    sub.add_parser("audit-list", help="审计日志列表")
    sub.add_parser("audit-clear", help="清除审计日志")

    # 公告
    sub.add_parser("announcement-list", help="公告列表")

    # 2FA
    sub.add_parser("twofa-list", help="2FA 配置列表")

    # SSO
    sub.add_parser("sso-list", help="SSO 提供商列表")

    # 元信息
    sub.add_parser("meta-list", help="元信息列表")

    # 设置
    sub.add_parser("setting-list", help="设置列表")

    # 树形展示
    p = sub.add_parser("tree", help="树形展示目录")
    p.add_argument("path", nargs="?", default="/")
    p.add_argument("--depth", type=int, default=2)

    # 刮削诊断
    p = sub.add_parser("diagnose-scrape", help="刮削诊断：检查目录刮削状态")
    p.add_argument("path")

    args = parser.parse_args()
    client = AlistClient(args.base_url, args.username, args.password, args.api_key, args.timeout)

    result = None
    # Normalize CLI aliases (e.g. "ls" → "list", "rm" → "remove")
    ALIAS_MAP = {"ls": "list", "rm": "remove"}
    action = ALIAS_MAP.get(args.action, args.action)

    if action == "login":
        result = client.login()
    elif action == "ping":
        result = client.ping()
    elif action == "list":
        result = client.list_files(args.path, getattr(args, "password", ""), getattr(args, "page", 1))
    elif action == "get":
        result = client.get_file(args.path, getattr(args, "password", ""))
    elif action == "search":
        result = client.search_files(args.keyword, args.scope)
    elif action == "mkdir":
        result = client.mkdir(args.path)
    elif action == "rename":
        result = client.rename(args.path, args.name)
    elif action == "move":
        result = client.move(args.src_dir, args.dst_dir, args.names)
    elif action == "recursive-move":
        result = client.recursive_move(args.src_dir, args.dst_dir)
    elif action == "copy":
        result = client.copy(args.src_dir, args.dst_dir, args.names)
    elif action == "remove":
        result = client.remove(args.dir, args.names)
    elif action == "dirs":
        result = client.dirs(args.path, getattr(args, "password", ""), getattr(args, "force_root", False))
    elif action == "offline-download":
        result = client.add_offline_download(args.urls, args.save_path, args.tool)
    elif action == "add-aria2":
        result = client.add_aria2(args.urls, args.save_path)
    elif action == "upload":
        result = client.upload_file(args.local_file, args.remote_dir)
    elif action == "download":
        result = client.download_file(args.remote_path, args.local_dir)
    elif action == "storage-list":
        result = client.storage_list()
    elif action == "storage-get":
        result = client.storage_get(args.id)
    elif action == "storage-refresh":
        result = client.storage_refresh()
    elif action == "storage-enable":
        result = client.storage_enable(args.id)
    elif action == "storage-disable":
        result = client.storage_disable(args.id)
    elif action == "storage-delete":
        result = client.storage_delete(args.id)
    elif action == "driver-list":
        result = client.driver_list()
    elif action == "driver-names":
        result = client.driver_names()
    elif action == "driver-info":
        result = client.driver_info(args.driver)
    elif action == "user-list":
        result = client.user_list()
    elif action == "user-get":
        result = client.user_get(args.id)
    elif action == "user-delete":
        result = client.user_delete(args.id)
    elif action == "task-upload":
        result = client.task_upload_list()
    elif action == "task-download":
        result = client.task_download_list()
    elif action == "task-copy":
        result = client.task_copy_list()
    elif action == "task-clear-done":
        result = client.task_clear_done()
    elif action == "task-clear-succeeded":
        result = client.task_clear_succeeded()
    elif action == "task-clear":
        result = client.task_clear()
    elif action == "index-progress":
        result = client.index_progress()
    elif action == "index-stop":
        result = client.index_stop()
    elif action == "index-clear":
        result = client.index_clear()
    elif action == "backup-list":
        result = client.backup_list()
    elif action == "backup-backup":
        result = client.backup_backup()
    elif action == "ssh-list":
        result = client.ssh_list()
    elif action == "audit-list":
        result = client.audit_list()
    elif action == "audit-clear":
        result = client.audit_clear()
    elif action == "announcement-list":
        result = client.announcement_list()
    elif action == "twofa-list":
        result = client.twofa_list()
    elif action == "sso-list":
        result = client.sso_list()
    elif action == "meta-list":
        result = client.meta_list()
    elif action == "setting-list":
        result = client.setting_list()
    elif action == "tree":
        output = client.tree(args.path, getattr(args, "depth", 2))
        print(output)
        return
    elif action == "diagnose-scrape":
        result = client.diagnose_scrape(args.path)

    output = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"结果已写入 {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
