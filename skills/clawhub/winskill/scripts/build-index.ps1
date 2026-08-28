<#
.SYNOPSIS
    Winskill 目录生成脚本 - 从模块 frontmatter 自动汇总主索引与子集分组
.DESCRIPTION
    扫描 references/modules/*.md 的 frontmatter，生成：
    1. SKILL.md 中的模块导航（按子集分组）
    2. 速查表
    3. 防止两处漂移（单一数据源）
#>

param(
    [string]$SkillRoot = (Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path))
)

$modulesDir = Join-Path $SkillRoot "references\modules"
$outputFile = Join-Path $SkillRoot "SKILL.md"

# 子集定义
$subsetNames = @{
    "disk-management" = "🖥️ 磁盘管理"
    "network-security" = "🔒 网络安全"
    "performance" = "📊 性能监控"
    "basic" = "🔧 基础运维"
    "advanced" = "🚀 高级功能"
}

$subsetOrder = @("disk-management", "network-security", "performance", "basic", "advanced")

# 扫描模块文件
$modules = Get-ChildItem -Path $modulesDir -Filter "module-*.md" | Sort-Object Name

$moduleData = @()

foreach ($file in $modules) {
    $content = Get-Content $file.FullName -Raw -Encoding utf8
    
    # 解析 frontmatter
    if ($content -match '---\s*\n(.*?)\n---') {
        $frontmatter = $matches[1]
        
        # 提取字段
        $id = if ($frontmatter -match 'id:\s*(.+)') { $matches[1].Trim() } else { "" }
        $name = if ($frontmatter -match 'name:\s*(.+)') { $matches[1].Trim() } else { "" }
        $description = if ($frontmatter -match 'description:\s*(.+)') { $matches[1].Trim() } else { "" }
        $keywords = if ($frontmatter -match 'keywords:\s*\[(.+?)\]') { 
            $matches[1] -split ',' | ForEach-Object { $_.Trim().Trim('"').Trim("'") }
        } else { @() }
        $permission = if ($frontmatter -match 'permission:\s*(.+)') { $matches[1].Trim() } else { "user" }
        $mode = if ($frontmatter -match 'mode:\s*(.+)') { $matches[1].Trim() } else { "readonly" }
        $subset = if ($frontmatter -match 'subset:\s*(.+)') { $matches[1].Trim() } else { "basic" }
        
        $moduleData += [PSCustomObject]@{
            Id = $id
            Name = $name
            Description = $description
            Keywords = $keywords
            Permission = $permission
            Mode = $mode
            Subset = subset
            File = $file.Name
        }
    }
}

# 按子集分组
$grouped = @{}
foreach ($s in $subsetOrder) {
    $grouped[$s] = @()
}
foreach ($m in $moduleData) {
    if ($grouped.ContainsKey($m.Subset)) {
        $grouped[$m.Subset] += $m
    }
}

# 生成导航 Markdown
$navLines = @()
$navLines += "## 📌 模块导航（点击直达，共 $($moduleData.Count) 个模块）"
$navLines += ""

foreach ($s in $subsetOrder) {
    $subsetName = $subsetNames[$s]
    $mods = $grouped[$s]
    if ($mods.Count -eq 0) { continue }
    
    $navLines += "**$subsetName（$($mods.Count)）：**"
    $links = $mods | ForEach-Object { 
        $anchor = $_.Id -replace 'module-', 'module-'
        "[$($_.Name)](#$anchor)" 
    }
    $navLines += ($links -join " · ")
    $navLines += ""
}

$navLines += "---"
$navLines += ""

$navBlock = $navLines -join "`n"

# 读取现有 SKILL.md
$existingContent = Get-Content $outputFile -Raw -Encoding utf8

# 替换导航部分（从 ## 📌 模块导航 到下一个 ---）
$navStart = $existingContent.IndexOf("## 📌 模块导航")
if ($navStart -ge 0) {
    $navEnd = $existingContent.IndexOf("---", $navStart)
    if ($navEnd -ge 0) {
        $navEnd = $existingContent.IndexOf("`n", $navEnd) + 1
        $newContent = $existingContent.Substring(0, $navStart) + $navBlock + $existingContent.Substring($navEnd)
        Set-Content -Path $outputFile -Value $newContent -Encoding utf8 -NoNewline
        Write-Host "✅ 已更新模块导航（$($moduleData.Count) 个模块，$($subsetOrder.Count) 个子集）"
    }
} else {
    Write-Host "⚠️ 未找到 ## 📌 模块导航 标记，请手动插入"
}
