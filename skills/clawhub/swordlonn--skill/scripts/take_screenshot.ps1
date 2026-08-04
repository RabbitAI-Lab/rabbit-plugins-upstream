# ============================================================
# WatchItAI - Windows Screenshot Helper (PowerShell)
#
# Usage:
#   powershell -ExecutionPolicy Bypass -File take_screenshot.ps1
#   powershell -ExecutionPolicy Bypass -File take_screenshot.ps1 -Mode temp
#   powershell -ExecutionPolicy Bypass -File take_screenshot.ps1 -Path "C:\Temp\screen.png"
#   powershell -ExecutionPolicy Bypass -File take_screenshot.ps1 -Mode temp -Region 100,200,800,600
#   powershell -ExecutionPolicy Bypass -File take_screenshot.ps1 -Mode temp -ActiveWindow
#   powershell -ExecutionPolicy Bypass -File take_screenshot.ps1 -WindowHandle 123456
# ============================================================

param(
    [ValidateSet("default", "temp")]
    [string]$Mode = "default",

    [string]$Path = "",

    [int[]]$Region = $null,

    [switch]$ActiveWindow,

    [int]$WindowHandle = 0
)

# Add required assemblies
Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Runtime.InteropServices

# Win32 API imports
$signature = @"
[DllImport("user32.dll")]
public static extern IntPtr GetForegroundWindow();

[DllImport("user32.dll")]
public static extern bool GetWindowRect(IntPtr hWnd, out RECT lpRect);

[StructLayout(LayoutKind.Sequential)]
public struct RECT
{
    public int Left;
    public int Top;
    public int Right;
    public int Bottom;
}
"@
$Win32 = Add-Type -MemberDefinition $signature -Name "Win32" -Namespace "WatchItAI" -PassThru

function Get-DefaultScreenshotDir {
    $pictures = [Environment]::GetFolderPath("MyPictures")
    if ($pictures -and (Test-Path $pictures)) {
        return $pictures
    }
    $desktop = [Environment]::GetFolderPath("Desktop")
    if ($desktop -and (Test-Path $desktop)) {
        return $desktop
    }
    return [Environment]::GetFolderPath("UserProfile")
}

function Get-GeneratedFilename {
    $timestamp = Get-Date -Format "yyyy-MM-dd at HH.mm.ss"
    return "watchitai $timestamp.png"
}

function Invoke-Screenshot {
    param(
        [string]$OutputPath,
        [System.Drawing.Rectangle]$Bounds,
        [bool]$IsRegion = $false
    )

    try {
        $bitmap = New-Object System.Drawing.Bitmap($Bounds.Width, $Bounds.Height)
        $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
        $graphics.CopyFromScreen($Bounds.Location, [System.Drawing.Point]::Empty, $Bounds.Size)
        $bitmap.Save($OutputPath, [System.Drawing.Imaging.ImageFormat]::Png)
        $graphics.Dispose()
        $bitmap.Dispose()
        return $true
    }
    catch {
        Write-Error "Screenshot failed: $_"
        return $false
    }
}

# Determine output path
if ($Path) {
    $outPath = $Path
    $outDir = Split-Path $outPath -Parent
    if (-not (Test-Path $outDir)) {
        New-Item -ItemType Directory -Path $outDir -Force | Out-Null
    }
}
elseif ($Mode -eq "temp") {
    $outDir = [System.IO.Path]::GetTempPath()
    $outPath = Join-Path $outDir (Get-GeneratedFilename)
}
else {
    $outDir = Get-DefaultScreenshotDir
    $outPath = Join-Path $outDir (Get-GeneratedFilename)
}

# Determine capture bounds
$bounds = $null

if ($Region -and $Region.Count -eq 4) {
    $x, $y, $w, $h = $Region
    $bounds = New-Object System.Drawing.Rectangle($x, $y, $w, $h)
}
elseif ($WindowHandle -ne 0) {
    $hWnd = [IntPtr]$WindowHandle
    $rect = New-Object "WatchItAI.Win32+RECT"
    if ($Win32::GetWindowRect($hWnd, [ref]$rect)) {
        $w = $rect.Right - $rect.Left
        $h = $rect.Bottom - $rect.Top
        $bounds = New-Object System.Drawing.Rectangle($rect.Left, $rect.Top, $w, $h)
    }
}
elseif ($ActiveWindow) {
    $hWnd = $Win32::GetForegroundWindow()
    $rect = New-Object "WatchItAI.Win32+RECT"
    if ($Win32::GetWindowRect($hWnd, [ref]$rect)) {
        $w = $rect.Right - $rect.Left
        $h = $rect.Bottom - $rect.Top
        $bounds = New-Object System.Drawing.Rectangle($rect.Left, $rect.Top, $w, $h)
    }
}
else {
    # Full screen (primary display)
    $screen = [System.Windows.Forms.Screen]::PrimaryScreen
    $bounds = $screen.Bounds
}

if (-not $bounds) {
    Write-Error "Failed to determine capture bounds."
    exit 1
}

# Capture
$success = Invoke-Screenshot -OutputPath $outPath -Bounds $bounds

if ($success) {
    Write-Output $outPath
}
else {
    Write-Error "Screenshot capture failed."
    exit 1
}
