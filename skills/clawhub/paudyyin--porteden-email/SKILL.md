# Porteden 多邮箱管理技能
## 功能说明
基于官方Porteden CLI实现的安全邮件管理工具，支持Gmail、Outlook、Exchange等主流邮箱平台，提供邮件读取、搜索、发送、附件处理、多账户管理等功能，凭证安全存储在系统密钥环，无明文泄露风险。

## 核心功能
✅ **邮件读取**：查看未读邮件、最新邮件、指定文件夹邮件，支持显示全文/摘要
✅ **智能搜索**：按发件人、主题、内容、时间、附件等多条件搜索历史邮件
✅ **邮件发送**：支持文本/HTML邮件、附件添加、抄送/密送
✅ **多账户管理**：一键切换不同邮箱账户，支持工作/生活邮箱分离
✅ **附件处理**：自动下载附件、批量导出附件
✅ **过滤器规则**：自动分类、标记、归档邮件

## 前置安装步骤
### 1. 安装Porteden CLI
#### 方式一：brew安装（推荐）
```powershell
brew install porteden/tap/porteden
```
#### 方式二：源码编译安装
```powershell
go install github.com/porteden/cli@latest
```
安装完成后验证：`porteden --version`

### 2. 登录认证
#### 方式一：浏览器登录（推荐，安全）
```powershell
porteden login
```
会自动打开浏览器，选择你要绑定的邮箱平台授权即可，凭证会自动加密存储在系统密钥环。

#### 方式二：API密钥登录
获取Porteden API密钥后配置环境变量：
```powershell
$env:PE_API_KEY = "你的API密钥"
```
可选配置：
```powershell
# 默认配置文件路径
$env:PE_CONFIG = "~/.porteden/config.json"
# 时区配置
$env:PE_TIMEZONE = "Asia/Shanghai"
# 默认账户
$env:PE_PROFILE = "work"
```

## 脚本路径
执行脚本位于：`D:\Users\yindb2\AppData\Roaming\mx\openclaw-home\yindb2\.openclaw\workspace\skills\porteden-email\scripts\porteden.ps1`

## 使用方法
### 基础命令格式
```powershell
powershell -ExecutionPolicy Bypass -File "<脚本路径>" <命令> [参数]
```

### 常用操作示例
#### 1. 查看最新邮件
```powershell
# 查看最新10封邮件
porteden list

# 查看未读邮件
porteden list --unread

# 查看指定数量邮件
porteden list --limit 20

# 显示邮件全文
porteden list --include-body
```

#### 2. 搜索邮件
```powershell
# 按主题搜索
porteden search --subject "会议"

# 按发件人搜索
porteden search --from "zhangsan@company.com"

# 按时间范围搜索
porteden search --after "2026-04-01" --before "2026-04-19"

# 搜索带附件的邮件
porteden search --has-attachment

# 组合条件搜索
porteden search --subject "项目" --from "manager@company.com" --after "2026-04-01"
```

#### 3. 发送邮件
```powershell
porteden send --to "lisi@example.com" --subject "项目进度汇报" --body "附件是本周项目进度，请查收。" --attach "D:\report.xlsx"

# 带抄送、密送
porteden send --to "lisi@example.com" --cc "wangwu@example.com" --bcc "manager@company.com" --subject "通知" --body "内容"
```

#### 4. 多账户管理
```powershell
# 列出所有已配置账户
porteden accounts list

# 切换默认账户
porteden accounts use "personal"

# 添加新账户
porteden accounts add "work2"
```

#### 5. 附件操作
```powershell
# 下载指定邮件的所有附件
porteden attachments download --message-id <邮件ID> --output "D:\attachments"

# 导出本周所有邮件附件
porteden attachments export --after "2026-04-15" --output "D:\weekly_attachments"
```

## 安全说明
🔒 所有邮箱凭证都加密存储在系统密钥环中，不会明文保存在本地
🔒 支持最小权限授权，仅授予需要的邮箱操作权限
🔒 不会上传任何邮件内容到第三方服务器，所有操作都在本地完成
🔒 可随时通过`porteden logout`清除所有凭证

## 配置文件
默认配置文件位于：`~/.porteden/config.json`，可以自定义默认账户、邮件同步规则、过滤器等。
