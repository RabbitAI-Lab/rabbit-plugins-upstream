# Porteden 邮件管理封装脚本
param(
    [Parameter(Position=0, Mandatory=$true)]
    [string]$Command,
    # list 命令参数
    [switch]$unread,
    [int]$limit = 10,
    [switch]$include_body,
    # search 命令参数
    [string]$subject = $null,
    [string]$from = $null,
    [string]$to = $null,
    [string]$after = $null,
    [string]$before = $null,
    [switch]$has_attachment,
    # send 命令参数
    [string]$to_addr = $null,
    [string]$cc = $null,
    [string]$bcc = $null,
    [string]$mail_subject = $null,
    [string]$body = $null,
    [string]$attach = $null,
    # accounts 命令参数
    [string]$profile = $null,
    # attachments 命令参数
    [string]$message_id = $null,
    [string]$output = $null,
    # 其他参数
    [parameter(ValueFromRemainingArguments = $true)]
    [string[]]$RemainingArgs
)

# 检查porteden是否安装
try {
    $null = Get-Command "porteden" -ErrorAction Stop
} catch {
    Write-Error "❌ Porteden CLI 未安装，请先按照SKILL.md中的步骤安装CLI并完成认证后再使用。"
    Write-Host "安装指引："
    Write-Host "1. brew install porteden/tap/porteden （推荐）"
    Write-Host "2. 或 go install github.com/porteden/cli@latest"
    exit 1
}

# 构建命令参数
$argsList = @($Command)

switch ($Command.ToLower()) {
    "list" {
        if ($unread) { $argsList += "--unread" }
        $argsList += "--limit", $limit
        if ($include_body) { $argsList += "--include-body" }
    }
    "search" {
        if ($subject) { $argsList += "--subject", "`"$subject`"" }
        if ($from) { $argsList += "--from", "`"$from`"" }
        if ($to) { $argsList += "--to", "`"$to`"" }
        if ($after) { $argsList += "--after", "`"$after`"" }
        if ($before) { $argsList += "--before", "`"$before`"" }
        if ($has_attachment) { $argsList += "--has-attachment" }
    }
    "send" {
        if (-not $to_addr -or -not $mail_subject -or -not $body) {
            Write-Error "❌ 发送邮件需要指定--to_addr、--mail_subject、--body参数"
            exit 1
        }
        $argsList += "--to", "`"$to_addr`""
        $argsList += "--subject", "`"$mail_subject`""
        $argsList += "--body", "`"$body`""
        if ($cc) { $argsList += "--cc", "`"$cc`"" }
        if ($bcc) { $argsList += "--bcc", "`"$bcc`"" }
        if ($attach) { $argsList += "--attach", "`"$attach`"" }
    }
    "accounts" {
        if ($RemainingArgs.Count -gt 0) {
            $argsList += $RemainingArgs
        }
        if ($profile) { $argsList += "use", "`"$profile`"" }
    }
    "attachments" {
        if ($RemainingArgs.Count -gt 0) {
            $argsList += $RemainingArgs
        }
        if ($message_id -and $output) {
            $argsList += "download", "--message-id", "`"$message_id`"", "--output", "`"$output`""
        }
    }
    "login" {}
    "logout" {}
    "version" {}
    default {
        Write-Error "❌ 不支持的命令：$Command"
        Write-Host "支持的命令：list, search, send, accounts, attachments, login, logout, version"
        exit 1
    }
}

# 添加剩余参数
if ($RemainingArgs.Count -gt 0 -and $Command.ToLower() -notin @("accounts", "attachments")) {
    $argsList += $RemainingArgs
}

try {
    Write-Host "🔄 正在执行邮件操作..."
    $fullCommand = "porteden $($argsList -join ' ')"
    Invoke-Expression $fullCommand
    if ($LASTEXITCODE -ne 0) {
        throw "操作失败，退出码：$LASTEXITCODE"
    }
} catch {
    Write-Error "❌ 邮件操作失败：$_"
    exit 1
}
