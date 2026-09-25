# organize-files.ps1 - File organizer (by type or by date)
# Usage:
#   powershell -ExecutionPolicy Bypass -File organize-files.ps1 -Dir . -DryRun
#   powershell -ExecutionPolicy Bypass -File organize-files.ps1 -Dir . -ByDate
param(
    [string]$Dir = ".",
    [switch]$ByDate,
    [switch]$DryRun,
    [switch]$Recurse
)

$ErrorActionPreference = "Stop"

$target = (Resolve-Path -LiteralPath $Dir).Path
$scriptFullName = $MyInvocation.MyCommand.Path

# --- Type -> category map ---
$typeMap = @{
    "jpg" = "Images"; "jpeg" = "Images"; "png" = "Images"; "gif" = "Images"
    "bmp" = "Images"; "webp" = "Images"; "svg" = "Images"; "ico" = "Images"
    "pdf" = "Documents"; "doc" = "Documents"; "docx" = "Documents"
    "xls" = "Documents"; "xlsx" = "Documents"; "ppt" = "Documents"
    "pptx" = "Documents"; "txt" = "Documents"; "md" = "Documents"
    "csv" = "Documents"; "odt" = "Documents"
    "mp4" = "Videos"; "avi" = "Videos"; "mkv" = "Videos"; "mov" = "Videos"
    "wmv" = "Videos"; "flv" = "Videos"; "webm" = "Videos"
    "mp3" = "Audio"; "wav" = "Audio"; "flac" = "Audio"; "aac" = "Audio"
    "ogg" = "Audio"; "m4a" = "Audio"
    "zip" = "Archives"; "rar" = "Archives"; "7z" = "Archives"
    "tar" = "Archives"; "gz" = "Archives"; "bz2" = "Archives"
    "py" = "Code"; "js" = "Code"; "ts" = "Code"; "java" = "Code"
    "c" = "Code"; "cpp" = "Code"; "h" = "Code"; "go" = "Code"; "rs" = "Code"
    "html" = "Code"; "css" = "Code"; "json" = "Code"; "xml" = "Code"
    "sh" = "Code"; "ps1" = "Code"; "sql" = "Code"
}

function Get-Category {
    param([System.IO.FileInfo]$File)
    if ($ByDate) {
        return $File.LastWriteTime.ToString("yyyy-MM")
    }
    if ($File.Extension) {
        $ext = $File.Extension.TrimStart(".").ToLower()
        if ($typeMap.ContainsKey($ext)) { return $typeMap[$ext] }
    }
    return "Others"
}

# --- Collect loose files ---
$files = Get-ChildItem -LiteralPath $target -File -Recurse:$Recurse | Where-Object {
    $_.Name -notlike ".*" -and
    $_.FullName -ne $scriptFullName -and
    $_.Name -ne "organize-report.md"
}

if ($files.Count -eq 0) {
    Write-Host "No files to organize in $target"
    exit 0
}

# --- Plan the moves ---
$plan = foreach ($f in $files) {
    $cat = Get-Category $f
    $destDir = Join-Path $target $cat
    $dest = Join-Path $destDir $f.Name

    $i = 1
    while (Test-Path -LiteralPath $dest) {
        $name = [System.IO.Path]::GetFileNameWithoutExtension($f.Name)
        $ext = $f.Extension
        $dest = Join-Path $destDir "$name ($i)$ext"
        $i++
    }

    [PSCustomObject]@{
        File     = $f.Name
        Category = $cat
        From     = $f.FullName
        To       = $dest
    }
}

# --- Show plan ---
Write-Host ""
Write-Host "===== Organization Plan ($($plan.Count) files) ====="
$plan | Group-Object Category | ForEach-Object {
    Write-Host ("  [{0}] {1} file(s)" -f $_.Name, $_.Count)
}

if ($DryRun) {
    Write-Host ""
    Write-Host "[DRY-RUN] Preview only - nothing was moved."
    exit 0
}

# --- Execute ---
$moved = 0
foreach ($p in $plan) {
    $destDir = Split-Path -Parent $p.To
    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    Move-Item -LiteralPath $p.From -Destination $p.To
    $moved++
}

# --- Report ---
$catRows = $plan | Group-Object Category | ForEach-Object { "| $($_.Name) | $($_.Count) |" }
$report = @"
# Organization Report

**Folder**: $target
**Mode**: $(if ($ByDate) { "by date (yyyy-MM)" } else { "by type" })
**Moved**: $moved / $($plan.Count) files

## Summary by category
| Category | Files |
|----------|-------|
$($catRows -join "`n")
"@
Set-Content -LiteralPath (Join-Path $target "organize-report.md") -Value $report -Encoding UTF8

Write-Host ""
Write-Host "Done: moved $moved files. Report: $(Join-Path $target 'organize-report.md')"
