#!/usr/bin/env python3
"""英文文案映射（中文即键模型）

规则：
- 键 = 脚本内 T("...") 的中文模板（含占位符时中英模板占位符名必须一致）
- 新增中文文案必须同步补此处映射（check_i18n_sync.py 覆盖检查强制）
- en.py 中不得存在未被任何 T() 引用的死键（覆盖检查 WARNING 提示清理）
- 翻译对照 i18n/en/glossary.md 术语表
"""

MESSAGES = {
    # ============== logout.py ==============
    "ℹ️  当前没有凭证，无需登出。": "ℹ️  No credentials found, nothing to log out.",
    "✅ 已清除凭证。": "✅ Credentials cleared.",
    "如需重新登录：python3 scripts/login.py":
        "To configure credentials again, follow the authentication setup of this skill.",

    # ============== login_url.py ==============
    "STS AssumeRole 失败: {message}": "STS AssumeRole failed: {message}",
    "STS AssumeRole 失败": "STS AssumeRole failed",
    "STS AssumeRole 请求异常: {error}": "STS AssumeRole request error: {error}",
    "请检查 AK/SK 和 ROLE_ARN": "Please check your AK/SK and ROLE_ARN",
    "缺少目标 URL 参数。用法: python3 login_url.py <target_url>":
        "Missing target URL parameter. Usage: python3 login_url.py <target_url>",
    "缺少凭证。请通过 OAuth 登录、配置 AK/SK 环境变量，或通过 Connector 获取临时密钥。":
        "Missing credentials. Please configure the AK/SK environment variables "
        "(TENCENTCLOUD_SECRET_ID / TENCENTCLOUD_SECRET_KEY).",
    "未配置角色信息。请选择以下方式之一:\\n\\n方式一: 设置角色名称（推荐）\\n"
    "  export TENCENTCLOUD_ROLE_NAME=\\\"AdvisorRole\\\"\\n\\n方式二: 设置完整 ARN\\n"
    "  export TENCENTCLOUD_ROLE_ARN=\\\"qcs::cam::uin/您的账号UIN:roleName/角色名\\\"\\n\\n"
    "方式三: 运行角色创建脚本（首次使用推荐）\\n  python3 scripts/create_role.py\\n\\n"
    "提示: 您可以在 CAM 控制台查看可用角色:\\n  https://console.cloud.tencent.com/cam/role":
        "Role information is not configured. Choose one of the following:\\n\\n"
        "Option 1: Set a role name (recommended)\\n"
        "  export TENCENTCLOUD_ROLE_NAME=\\\"AdvisorRole\\\"\\n\\n"
        "Option 2: Set the full ARN\\n"
        "  export TENCENTCLOUD_ROLE_ARN=\\\"qcs::cam::uin/your-account-UIN:roleName/role-name\\\"\\n\\n"
        "Option 3: Run the role creation script (recommended for first use)\\n"
        "  python3 scripts/create_role.py\\n\\n"
        "Tip: You can view available roles in the CAM console:\\n"
        "  https://console.tencentcloud.com/cam/role",

    # ============== tcloud_async_task.py ==============
    "ChatID 为必填参数": "ChatID is a required parameter",
    "SessionID 为必填参数": "SessionID is a required parameter",
    "无法导入 tcloud_api 模块，请确保 scripts 目录在 Python 路径中":
        "Cannot import the tcloud_api module; make sure the scripts directory is on the Python path",
    "轮询超时（{timeout}秒），任务可能仍在执行中":
        "Polling timed out ({timeout}s); the task may still be running",
    "用法:\n  python3 tcloud_async_task.py query <chat_id> <session_id>\n"
    "  python3 tcloud_async_task.py cancel <chat_id> [session_id]\n"
    "  python3 tcloud_async_task.py poll <chat_id> <session_id> [timeout]":
        "Usage:\n  python3 tcloud_async_task.py query <chat_id> <session_id>\n"
        "  python3 tcloud_async_task.py cancel <chat_id> [session_id]\n"
        "  python3 tcloud_async_task.py poll <chat_id> <session_id> [timeout]",
    "timeout 必须是整数": "timeout must be an integer",

    # ============== credential_manager.py ==============
    "未知服务端错误": "Unknown server error",
    "网络连接失败: {reason}": "Network connection failed: {reason}",
    "获取授权 URL 失败: {error}": "Failed to get the authorization URL: {error}",
    "exchange_token 失败: {error}": "exchange_token failed: {error}",
    "获取临时密钥失败: {error}": "Failed to get the temporary key: {error}",
    "refreshToken 已过期或无效: {error}。请重新授权登录。":
        "The refreshToken is expired or invalid: {error}. Please authorize again.",
    "OAuth 临时密钥已过期且自动刷新失败，请重新授权登录。":
        "The OAuth temporary key has expired and automatic refresh failed. Please authorize again.",
    "Connector 临时密钥（OneId 方案）已过期，请通过 "
    "CloudQConnector_get_available_tmp_secret 重新获取。":
        "The Connector temporary key (OneId) has expired. Please obtain a new one via "
        "CloudQConnector_get_available_tmp_secret.",

    # ============== create_role.py ==============
    "未知参数: {arg}": "Unknown argument: {arg}",
    "未配置 TENCENTCLOUD_SECRET_ID 或 TENCENTCLOUD_SECRET_KEY":
        "TENCENTCLOUD_SECRET_ID or TENCENTCLOUD_SECRET_KEY is not configured",
    "无法获取账号 UIN": "Cannot get the account UIN",
    "无法找到可用的角色名称（已尝试 advisor ~ advisor19），"
    "请到 CAM 控制台手动管理: https://console.cloud.tencent.com/cam/role":
        "No available role name found (tried advisor ~ advisor19). "
        "Please manage roles manually in the CAM console: https://console.tencentcloud.com/cam/role",
    "策略 {policy} 关联失败: {message}": "Failed to attach policy {policy}: {message}",
    "腾讯云智能顾问助手角色（由 tencent-cloudq skill 创建）":
        "Tencent Cloud Smart Advisor assistant role (created by the tencent-cloudq skill)",
    "角色 {role} 创建失败: {message}": "Failed to create role {role}: {message}",
    "未知错误": "Unknown error",

    # ============== tcloud_api.py ==============
    "OAuth 凭证已过期，需要重新授权登录。{error}":
        "OAuth credentials have expired; re-authorization is required. {error}",
    "未找到凭证，请先通过 OAuth 登录或配置 AK/SK 环境变量。":
        "No credentials found. Please configure the AK/SK environment variables "
        "(TENCENTCLOUD_SECRET_ID / TENCENTCLOUD_SECRET_KEY).",
    "未配置凭证。请通过 OAuth 登录或配置 AK/SK 环境变量。\n"
    "OAuth 登录: python3 scripts/login.py\n"
    "密钥获取: https://console.cloud.tencent.com/cam/capi":
        "Credentials not configured. Please set the AK/SK environment variables:\n"
        "TENCENTCLOUD_SECRET_ID / TENCENTCLOUD_SECRET_KEY\n"
        "Get keys: https://console.tencentcloud.com/cam/capi",
    "如需调用 {service} 服务，请配置 AK/SK 环境变量。":
        "To call the {service} service, please configure AK/SK environment variables.",
    "CloudQ 不支持调用 {service} 服务。": "CloudQ does not support calling the {service} service.",
    "当前凭证不允许调用 {service} 服务（允许: {allowed}）。{hint}":
        "The current credentials are not allowed to call the {service} service (allowed: {allowed}). {hint}",
    "HTTP 请求失败 (状态码 {code}): {reason}": "HTTP request failed (status {code}): {reason}",
    "网络连接失败，请检查网络和域名 {host} 是否可达: {reason}":
        "Network connection failed. Please check the network and whether {host} is reachable: {reason}",
    "请求异常: {error}": "Request error: {error}",
    "响应不是有效的 JSON": "The response is not valid JSON",
    "缺少必要参数。用法: python3 tcloud_api.py <service> <host> <action> <version> [payload] [region]":
        "Missing required arguments. Usage: python3 tcloud_api.py <service> <host> <action> <version> [payload] [region]",

    # ============== tcloud_sse_api.py ==============
    "凭证已过期。{error}": "Credentials have expired. {error}",
    "未找到凭证，请先通过 OAuth 登录、配置 AK/SK 环境变量，"
    "或通过 Connector 获取临时密钥。":
        "No credentials found. Please configure the AK/SK environment variables "
        "(TENCENTCLOUD_SECRET_ID / TENCENTCLOUD_SECRET_KEY).",
    "请配置环境变量 AK/SK（国际站当前唯一支持的鉴权方式）：":
        "Configure the AK/SK environment variables (the only supported auth method "
        "on the international site):",
    "检测到本地凭证文件，国际站仅支持 AK/SK，已忽略":
        "Local credential file detected; the international site supports AK/SK only — ignored",
    "当前授权方式的凭证缺失，无法调用 API。请检查凭证配置是否正确。"
    "如需更换授权方式，请明确告知。":
        "Credentials for the current auth method are missing, so the API cannot be called. "
        "Please check the credential configuration. If you want to switch auth methods, say so explicitly.",
    "国际站不支持免密登录，已跳过角色检测":
        "Password-free login is not available on the international site — role check skipped",
    "环境就绪（国际站：智能顾问已开通 + API 查询可用）":
        "Environment ready (international site: Smart Advisor enabled + API queries available)",
    "接口返回非 SSE 格式且无法解析为 JSON: {body}":
        "The API returned a non-SSE format that cannot be parsed as JSON: {body}",
    "解析响应失败: {error}": "Failed to parse the response: {error}",
    "用法: python3 tcloud_sse_api.py <question> --source <platform> "
    "--session-id <uuid>":
        "Usage: python3 tcloud_sse_api.py <question> --source <platform> "
        "--session-id <uuid>",
    "缺少必填参数 --session-id。"
    "请通过 SID=$(python3 -c 'import uuid;print(uuid.uuid4())') 生成后传入。":
        "Missing the required argument --session-id. "
        "Generate one with SID=$(python3 -c 'import uuid;print(uuid.uuid4())') and pass it in.",

    # ============== login.py ==============
    "服务端未返回有效的授权 URL": "The server did not return a valid authorization URL",
    "授权码为空": "The authorization code is empty",
    "登录成功": "Login successful",
    "未找到 OAuth 凭证": "No OAuth credentials found",
    "刷新后未找到凭证": "Credentials not found after refresh",
    "refreshToken 已过期，需要重新登录: {error}":
        "The refreshToken has expired; re-login is required: {error}",
    "请执行 python3 login.py --authorize-url 重新授权":
        "Please run python3 login.py --authorize-url to re-authorize",
    "请检查网络连接，或执行 python3 login.py --authorize-url 重新授权":
        "Please check the network connection, or run python3 login.py --authorize-url to re-authorize",
    "临时密钥已过期，自动刷新未触发":
        "The temporary key has expired and automatic refresh was not triggered",
    "请执行 python3 login.py --refresh 手动刷新，或重新登录":
        "Please run python3 login.py --refresh to refresh manually, or log in again",
    "未找到 OAuth 凭证，请先登录": "No OAuth credentials found; please log in first",
    "凭证刷新成功": "Credentials refreshed successfully",
    "refreshToken 已过期，请重新登录: {error}":
        "The refreshToken has expired; please log in again: {error}",
    "  ☁️ CloudQ OAuth 登录": "  ☁️ CloudQ OAuth Login",
    "  ℹ️  检测到已有 OAuth 凭证。": "  ℹ️  Existing OAuth credentials detected.",
    "  是否重新登录？(y/N) > ": "  Log in again? (y/N) > ",
    "  已取消。": "  Cancelled.",
    "  ◦ 获取授权链接...": "  ◦ Getting the authorization link...",
    "  ◦ 正在打开浏览器...": "  ◦ Opening the browser...",
    "  ⚠️  无法自动打开浏览器，请手动访问以下链接：":
        "  ⚠️  Cannot open the browser automatically; please visit the link below manually:",
    "  请在浏览器中打开以下链接完成授权：":
        "  Open the following link in a browser to complete authorization:",
    "  完成授权后，页面会显示一段授权码。":
        "  After authorization, the page will display an authorization code.",
    "  请复制并粘贴到下方：": "  Please copy and paste it below:",
    "  授权码 > ": "  Authorization code > ",
    "未输入授权码": "No authorization code entered",
    "  ◦ 用授权码换取 token...": "  ◦ Exchanging the code for a token...",
    "  ◦ 获取临时密钥...": "  ◦ Getting the temporary key...",
    "  ✅ 登录成功！": "  ✅ Login successful!",
    "  凭证已保存到 ~/.tencent-cloudq/credential.json":
        "  Credentials saved to ~/.tencent-cloudq/credential.json",
    "  临时密钥将在过期前自动刷新，您无需重复登录。":
        "  The temporary key refreshes automatically before expiry; no repeated login needed.",
    "\n  已取消登录。": "\n  Login cancelled.",
    "  ❌ 登录失败：{error}": "  ❌ Login failed: {error}",
    "缺少授权码参数: python3 login.py --save '<授权码>'":
        "Missing the authorization code argument: python3 login.py --save '<authorization-code>'",
    "CloudQ OAuth 登录": "CloudQ OAuth Login",
    "非交互式子命令（供 Agent 调用）：": "Non-interactive subcommands (for Agent use):",
    "  python3 login.py --authorize-url              # 获取授权 URL":
        "  python3 login.py --authorize-url              # Get the authorization URL",
    "  python3 login.py --save '<授权码>'             # 用授权码换取凭证":
        "  python3 login.py --save '<authorization-code>'  # Exchange the code for credentials",
    "  python3 login.py --status                      # 查看凭证状态":
        "  python3 login.py --status                      # Show credential status",
    "  python3 login.py --refresh                     # 主动刷新凭证":
        "  python3 login.py --refresh                     # Refresh credentials now",
    "交互式登录（仅供终端手动使用）：": "Interactive login (for manual terminal use only):",
    "  python3 login.py                               # 打开浏览器授权":
        "  python3 login.py                               # Open the browser to authorize",
    "  python3 login.py --no-browser                  # 手动模式":
        "  python3 login.py --no-browser                  # Manual mode",
    "  python3 login.py --site=intl                   # 国际站":
        "  python3 login.py --site=intl                   # International site",

    # ============== cleanup.py（抽取翻译合并） ==============
    '# 腾讯云智能顾问 - 环境变量清理脚本': '# Tencent Cloud Smart Advisor - environment variable cleanup script',
    '# 腾讯云智能顾问 - 环境变量清理脚本 (PowerShell)': '# Tencent Cloud Smart Advisor - environment variable cleanup script (PowerShell)',
    '# 自动生成，执行后可删除此文件': '# Auto-generated; you can delete this file after running it',
    '(空目录)': '(empty directory)',
    '1. 配置目录': '1. Config directory',
    '2. 凭证文件': '2. Credentials file',
    '3. 临时缓存': '3. Temporary cache',
    '4. 云端 CAM 角色': '4. Cloud CAM role',
    '5. 环境变量': '5. Environment variables',
    '不存在，跳过': 'does not exist, skipped',
    '临时缓存': 'temporary cache',
    '云端角色': 'cloud role',
    '云端角色 {role} 已删除': 'Cloud role {role} deleted',
    '凭证文件': 'credentials file',
    '凭证类型: {type}': 'Credential type: {type}',
    '删除失败 - {error}': 'failed to delete - {error}',
    '删除角色失败: {message}': 'Failed to delete role: {message}',
    '名称: {role}': 'Name: {role}',
    '如果变量写在 ~/.bashrc、~/.zshrc 或系统环境中，请手动移除对应行。': 'If the variables are defined in ~/.bashrc, ~/.zshrc, or system environment files, remove the corresponding lines manually.',
    '如需删除云端角色，请设置 TENCENTCLOUD_SECRET_ID 和 TENCENTCLOUD_SECRET_KEY 后重试': 'To delete the cloud role, set TENCENTCLOUD_SECRET_ID and TENCENTCLOUD_SECRET_KEY, then retry',
    '如需同时删除云端角色，请添加 --cloud 参数': 'To also delete the cloud role, add the --cloud argument',
    '已删除': 'deleted',
    '已清理 {count} 个环境变量（仅影响当前会话）': 'Cleaned up {count} environment variables (current session only)',
    '已清除 {var}': 'Cleared {var}',
    '已生成 PowerShell 清理脚本: {path}': 'PowerShell cleanup script generated: {path}',
    '已生成清理脚本: {path}': 'Cleanup script generated: {path}',
    '当前配置:': 'Current configuration:',
    '描述: {description}': 'Description: {description}',
    '提示: 使用 --all 跳过确认，--cloud 同时删除云端角色': 'Tip: use --all to skip confirmations, and --cloud to also delete the cloud role',
    '无描述': 'no description',
    '无法加载 tcloud_api 模块': 'Failed to load the tcloud_api module',
    '未指定 --cloud 参数，跳过云端角色清理': '--cloud not specified, skipping cloud role cleanup',
    '未检测到已设置的 TENCENTCLOUD_* 环境变量，跳过': 'No TENCENTCLOUD_* environment variables detected, skipping',
    '未知': 'unknown',
    '未配置 AK/SK 环境变量，跳过云端角色清理': 'AK/SK environment variables not configured, skipping cloud role cleanup',
    '查询角色失败: {message}': 'Failed to query role: {message}',
    '检测到 {count} 个已设置的环境变量:': 'Detected {count} environment variable(s) in use:',
    '检测到角色:': 'Detected role:',
    '正在删除角色 {role} ...': 'Deleting role {role} ...',
    '正在检查角色 {role} ...': 'Checking role {role} ...',
    '注意': 'Note',
    '清理完成: {cleaned}/{total} 项已清理': 'Cleanup complete: {cleaned}/{total} item(s) cleaned',
    '环境变量': 'environment variables',
    '环境变量存在于 shell 进程中，Python 脚本无法直接修改父 shell。': 'Environment variables live in the shell process; a Python script cannot modify the parent shell directly.',
    '用户跳过': 'skipped by user',
    '确认删除 {path} ?': 'Confirm deletion of {path} ?',
    '确认删除云端角色 {role} ? (此操作不可恢复)': 'Confirm deletion of cloud role {role} ? (this operation cannot be undone)',
    '确认删除凭证文件?': 'Confirm deletion of the credentials file?',
    '确认清理以上 {count} 个环境变量?': 'Clean up the {count} environment variables above?',
    '腾讯云智能顾问 - 配置清理': 'Tencent Cloud Smart Advisor - configuration cleanup',
    '角色 ARN:  {arn}': 'Role ARN:  {arn}',
    '角色 {role} 不存在，无需删除': 'Role {role} does not exist; nothing to delete',
    '角色名称:  {role}': 'Role name:  {role}',
    '请在 PowerShell 中执行:': 'Run it in PowerShell:',
    '请在当前终端执行:': 'Run it in the current terminal:',
    '请执行上方命令完成清理（仅影响当前终端会话）。': 'Run the command above to complete the cleanup (current terminal session only).',
    '账号 UIN:  {uin}': 'Account UIN:  {uin}',
    '路径: {path}': 'Path: {path}',
    '配置时间:  {time}': 'Configured at:  {time}',
    '配置目录': 'config directory',

    # ============== check_env.py（抽取翻译合并） ==============
    '1. 检查运行环境': '1. Checking runtime environment',
    '2. 检查 Skill 版本': '2. Checking Skill version',
    '3. 检查凭证配置': '3. Checking credentials configuration',
    '4. 验证凭证有效性': '4. Verifying credentials',
    '5. 检查智能顾问开通状态': '5. Checking Smart Advisor status',
    '6. 免密登录角色': '6. Password-free login role',
    '6. 检查免密登录角色配置': '6. Checking password-free login role configuration',
    '7. 验证角色扮演': '7. Verifying role assumption',
    '=== Changelog（变更日志）===': '=== Changelog ===',
    '=== 检测完成 ===': '=== Environment check completed ===',
    'AK/SK 密钥': 'AK/SK key',
    'CloudQ 所有功能均依赖智能顾问服务，必须先开通才能使用': 'All CloudQ features depend on the Smart Advisor service; it must be enabled before use',
    'Connector 临时密钥': 'Connector temporary key',
    'OAuth / Connector 模式下跳过角色检测（临时密钥无 cam/sts 权限）': 'Role check skipped in OAuth / Connector mode (temporary key has no cam/sts permissions)',
    'OAuth 凭证': 'OAuth credentials',
    'Python 版本过低: {version}，需要 Python 3.7+': 'Python version too old: {version}, Python 3.7+ required',
    'ROLE_ARN 已通过环境变量配置': 'ROLE_ARN configured via environment variable',
    'ROLE_NAME 已配置: {role}': 'ROLE_NAME configured: {role}',
    'SecretId 已配置: {masked_id}': 'SecretId configured: {masked_id}',
    'SecretKey 已配置: ****': 'SecretKey configured: ****',
    'refreshToken 已过期，需要重新登录': 'refreshToken expired, re-login required',
    '{cred_mode}验证通过': '{cred_mode} verification passed',
    '{credential_label}文件已存在': '{credential_label} file exists',
    '临时密钥 Token 已配置': 'Temporary key token configured',
    '临时密钥即将过期，尝试自动刷新...': 'Temporary key about to expire, attempting auto-refresh...',
    '临时密钥有效期剩余: {minutes} 分钟': 'Temporary key valid for {minutes} more minutes',
    '免密登录功能需要一个支持控制台登录的 CAM 角色（可选，不影响基本功能）': 'Password-free login requires a CAM role that supports console login (optional, does not affect basic features)',
    '免密登录角色已配置': 'Password-free login role configured',
    '免密登录角色未配置': 'Password-free login role not configured',
    '免密登录角色未配置（仅影响免密登录链接生成，不影响 CloudQ 基本功能）': 'Password-free login role not configured (only affects password-free login link generation, does not affect basic CloudQ features)',
    '免密登录链接功能仅在 AK/SK 模式下可用': 'The password-free login link feature is only available in AK/SK mode',
    '凭证无效: {error_code}': 'Invalid credentials: {error_code}',
    '凭证验证通过（鉴权成功）': 'Credentials verified (authentication succeeded)',
    '凭证验证通过，接口调用成功': 'Credentials verified, API call succeeded',
    '刷新后凭证文件丢失': 'Credential file lost after refresh',
    '刷新成功，有效期剩余: {minutes} 分钟': 'Refresh succeeded, valid for {minutes} more minutes',
    '前往 CloudQ 控制台 → 拓展 → Channels 集成 → OneID，绑定 WorkBuddy OneID 应用后，': 'Go to CloudQ console → Extensions → Channels integration → OneID, bind the WorkBuddy OneID application,',
    '发现新版本: {local_ver} → {remote_ver}': 'New version available: {local_ver} → {remote_ver}',
    '可能原因：当前凭证无智能顾问相关权限': 'Possible cause: current credentials lack Smart Advisor permissions',
    '可选：执行角色创建步骤以启用免密登录功能': 'Optional: run the role creation step to enable password-free login',
    '复制返回的 MCP 配置，在 WorkBuddy「连接器」→「自定义连接器」→「配置 MCP」中粘贴、保存并点击「连接」。': 'Copy the returned MCP configuration, then paste, save, and click "Connect" in WorkBuddy "Connectors" → "Custom Connector" → "Configure MCP".',
    '如需启用免密登录，请执行: python3 {path}': 'To enable password-free login, run: python3 {path}',
    '密钥获取地址: https://console.cloud.tencent.com/cam/capi': 'Get your API key at: https://console.tencentcloud.com/cam/capi',
    '将使用{credential_label}继续': 'Continuing with {credential_label}',
    '尝试查找其他支持控制台登录的角色...': 'Trying to find another role that supports console login...',
    '已跳过版本更新检查（--skip-update）': 'Version update check skipped (--skip-update)',
    '建议前往 SkillHub 或 ClawHub 更新此 Skill': 'It is recommended to update this Skill via SkillHub or ClawHub',
    '开通方式：请在对话中同意开通，或运行以下命令：': 'To enable it: agree in the conversation, or run the following command:',
    '当前已是最新版本: {local_ver}': 'Already up to date: {local_ver}',
    '当前版本: {local_ver}': 'Current version: {local_ver}',
    '接口调用失败，请检查网络连接': 'API call failed, please check your network connection',
    '接口返回业务错误: {error_code}（不影响鉴权）': 'API returned a business error: {error_code} (does not affect authentication)',
    '方式一：OAuth 浏览器授权（推荐，无需密钥）': 'Method 1: OAuth browser authorization (recommended, no key required)',
    '方式三：企业 OneID 授权': 'Method 3: Enterprise OneID authorization',
    '方式二：配置环境变量 AK/SK': 'Method 2: Configure AK/SK environment variables',
    '无法获取远端版本信息': 'Unable to fetch remote version information',
    '智能顾问已开通': 'Smart Advisor enabled',
    '智能顾问开通失败: {code} - {message}': 'Failed to enable Smart Advisor: {code} - {message}',
    '智能顾问开通成功！': 'Smart Advisor enabled successfully!',
    '智能顾问未开通': 'Smart Advisor not enabled',
    '最新版本: {remote_ver}': 'Latest version: {remote_ver}',
    '未找到 _meta.json 或版本信息缺失': '_meta.json not found or version information missing',
    '未找到任何支持控制台登录的角色': 'No roles supporting console login found',
    '未找到本地凭证': 'No local credentials found',
    '未检测到 {role} 角色': 'Role {role} not detected',
    '未配置以下环境变量: {missing}': 'The following environment variables are not configured: {missing}',
    '未配置环境变量: {missing}': 'Environment variables not configured: {missing}',
    '本地和远端版本信息均无法获取': 'Neither local nor remote version information could be retrieved',
    '本地版本: {local_ver}': 'Local version: {local_ver}',
    '本地版本: {local_ver} | 远端版本: {remote_ver}': 'Local version: {local_ver} | Remote version: {remote_ver}',
    '本地版本: {local_ver}，但无法获取远端版本信息': 'Local version: {local_ver}, but unable to fetch remote version information',
    '本地版本检查: {local_error}': 'Local version check: {local_error}',
    '本地缺少版本元数据，检测到远端最新版本: {remote_ver}': 'Local version metadata missing; latest remote version detected: {remote_ver}',
    '架构图共享协作已开启': 'Architecture diagram sharing and collaboration enabled',
    '架构图共享协作未开启（不影响 CloudQ 基本功能）': 'Architecture diagram sharing and collaboration not enabled (does not affect basic CloudQ features)',
    '查询智能顾问开通状态失败: {error_code}': 'Failed to query Smart Advisor status: {error_code}',
    '查询智能顾问开通状态失败，请检查网络连接': 'Failed to query Smart Advisor status, please check your network connection',
    '检查 {role} 角色是否存在...': 'Checking whether role {role} exists...',
    '检查本地凭证...': 'Checking local credentials...',
    '检测到可用角色 {name}（支持控制台登录），自动配置': 'Detected usable role {name} (console login supported), configured automatically',
    '检测到已有角色 {role}（支持控制台登录），自动配置': 'Detected existing role {role} (console login supported), configured automatically',
    '正在开通智能顾问...': 'Enabling Smart Advisor...',
    '版本检查跳过，继续后续检测...': 'Version check skipped, continuing with remaining checks...',
    '版本检查返回未知状态: {status}': 'Version check returned unknown status: {status}',
    '版本比较跳过，继续后续检测...': 'Version comparison skipped, continuing with remaining checks...',
    '环境基本就绪（智能顾问已开通，API 查询可用）': 'Environment mostly ready (Smart Advisor enabled, API queries available)',
    '环境就绪，所有功能可用（智能顾问已开通 + API 查询 + 免密登录）': 'Environment ready, all features available (Smart Advisor enabled + API queries + password-free login)',
    '环境检测未通过': 'Environment check failed',
    '策略 {policy_name} 关联失败: {err_msg}': 'Failed to attach policy {policy_name}: {err_msg}',
    '缺少角色名参数': 'Missing role name parameter',
    '自动刷新失败: {error}，尝试继续使用当前凭证': 'Auto-refresh failed: {error}, trying to continue with current credentials',
    '获取本地凭证失败: {error}': 'Failed to obtain local credentials: {error}',
    '角色 {role} 存在但不支持控制台登录': 'Role {role} exists but does not support console login',
    '角色已配置（来自配置文件）: {role}': 'Role configured (from config file): {role}',
    '角色扮演验证失败: {message}': 'Role assumption verification failed: {message}',
    '角色扮演验证异常: {error}': 'Role assumption verification error: {error}',
    '角色扮演验证返回格式异常': 'Role assumption verification returned an unexpected format',
    '角色扮演验证通过，免密登录功能正常': 'Role assumption verified, password-free login works properly',
    '角色策略检查通过': 'Role policy check passed',
    '请前往 SkillHub 或 ClawHub 更新此 Skill': 'Please update this Skill via SkillHub or ClawHub',
    '请在 WorkBuddy 中重新连接 CloudQ Connector': 'Please reconnect the CloudQ Connector in WorkBuddy',
    '请将腾讯云 API 密钥写入 shell 配置文件：': 'Please add the Tencent Cloud API key to your shell configuration file:',
    '请执行: python3 {path}': 'Please run: python3 {path}',
    '请根据上方提示完成初始化': 'Please complete initialization following the instructions above',
    '请检查密钥是否正确: https://console.cloud.tencent.com/cam/capi': 'Please check that your key is correct: https://console.tencentcloud.com/cam/capi',
    '请选择以下方式之一配置凭证：': 'Configure credentials using one of the following methods:',
    '请重新登录: python3 {path}': 'Please log in again: python3 {path}',
    '账号 UIN: {account_uin}': 'Account UIN: {account_uin}',
    '远端最新版本: {remote_ver}': 'Latest remote version: {remote_ver}',
    '远端检查: {error}': 'Remote check: {error}',
    '配置已保存到 {path}': 'Configuration saved to {path}',
}
