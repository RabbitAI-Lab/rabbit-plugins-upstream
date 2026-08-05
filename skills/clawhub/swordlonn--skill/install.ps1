# ============================================================
# WatchItAI Skill - Install to Trae global skills directory (Windows PowerShell)
#
# The skill uses a self-contained Go binary — no npm install needed.
#
# Usage (Run in PowerShell):
#   powershell -ExecutionPolicy Bypass -File .\install.ps1
# ============================================================

param(
    [string]$TraeSkillsDir = "$env:USERPROFILE\.trae-cn\skills"
)

$ErrorActionPreference = "Stop"
$SkillName = "watchitai"
$SourceDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$TargetDir = Join-Path $TraeSkillsDir $SkillName

Write-Host "📦 Installing WatchItAI skill to Trae..." -ForegroundColor Cyan
Write-Host "   Source: $SourceDir"
Write-Host "   Target: $TargetDir"
Write-Host ""

# ---- Remove existing install ---------------------------------------------
if (Test-Path $TargetDir) {
    Write-Host "🗑️  Removing existing installation..."
    Remove-Item -Recurse -Force $TargetDir
}

# ---- Create target directory ---------------------------------------------
New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null

# ---- Copy skill files (excluding dev-only files) -------------------------
Write-Host "📋 Copying skill files..."

$exclude = @(
    "node_modules",
    "install.sh",
    "install.ps1",
    "test-ws.js",
    "test_capture.cjs",
    "test_control.cjs",
    "test-platform.js",
    "index.js",
    ".git",
    ".trae",
    ".env",
    "*.tsbuildinfo",
    "data"
)

Get-ChildItem -Path $SourceDir -Recurse -File | Where-Object {
    $rel = $_.FullName.Substring($SourceDir.Length + 1)
    $skip = $false
    foreach ($ex in $exclude) {
        if ($rel -like "$ex*" -or $rel -like "*\$ex" -or $rel -like "*\$ex\*") {
            $skip = $true; break
        }
    }
    -not $skip
} | ForEach-Object {
    $rel = $_.FullName.Substring($SourceDir.Length + 1)
    $dest = Join-Path $TargetDir $rel
    $destDir = Split-Path -Parent $dest
    if (!(Test-Path $destDir)) {
        New-Item -ItemType Directory -Force -Path $destDir | Out-Null
    }
    Copy-Item -Force $_.FullName $dest
}

# ---- Detect platform and verify binary -----------------------------------
$arch = if ([Environment]::Is64BitOperatingSystem) { "amd64" } else { "x86" }
$binaryName = "watchitai-windows-$arch.exe"
$binaryPath = Join-Path $TargetDir "bin\$binaryName"

if (Test-Path $binaryPath) {
    Write-Host "✅ Binary found: $binaryName"
    try {
        & $binaryPath version
    } catch {
        Write-Host "⚠️  Binary not executable: $_" -ForegroundColor Yellow
    }
} else {
    Write-Host "⚠️  Binary not found for platform: windows/$arch" -ForegroundColor Yellow
    Write-Host "   Expected: $binaryPath"
    Write-Host "   Please re-download the skill package from https://watchitai.net"
}

Write-Host ""
Write-Host "✅ Installation complete! No Node.js, no npm install needed."
Write-Host ""
Write-Host "📁 Installed files:"
Get-ChildItem -Path $TargetDir | Select-Object -First 15 Name, Length
Write-Host ""
Write-Host "📄 SKILL.md frontmatter:"
Get-Content (Join-Path $TargetDir "SKILL.md") -TotalCount 4
Write-Host ""
Write-Host "🎉 WatchItAI skill installed successfully!" -ForegroundColor Green
Write-Host "   The skill uses a self-contained Go binary (watchitai-windows-amd64.exe)."
Write-Host "   Usage: run.cmd share"
