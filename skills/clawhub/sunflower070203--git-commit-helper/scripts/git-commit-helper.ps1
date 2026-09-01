[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateSet('analyze', 'commit')]
    [string]$Mode,

    [Parameter(Mandatory = $false)]
    [string]$MessageFile,

    [Parameter(Mandatory = $false)]
    [string[]]$Paths
)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = 'Continue'

function Write-Err {
    param([string]$Text)
    [Console]::Error.WriteLine($Text)
}

function Get-NumStatMap {
    param([string[]]$DiffArgs)
    $map = @{}
    $lines = & git diff --numstat @DiffArgs 2>$null
    if ($LASTEXITCODE -ne 0) { return $map }
    foreach ($line in $lines) {
        $parts = $line -split "`t"
        if ($parts.Count -ge 3) {
            $map[$parts[2]] = @{ Add = $parts[0]; Del = $parts[1] }
        }
    }
    return $map
}

function Format-Stat {
    param($Stat)
    if ($null -eq $Stat -or $Stat.Add -eq '-') { return '' }
    return (' (+' + $Stat.Add + '/-' + $Stat.Del + ')')
}

if ($Mode -eq 'commit') {
    try {
        if ([string]::IsNullOrWhiteSpace($MessageFile)) {
            Write-Err '[git-commit-helper] error: -MessageFile is required'
            exit 2
        }
        if (-not (Test-Path -LiteralPath $MessageFile)) {
            Write-Err '[git-commit-helper] error: message file not found: ' + $MessageFile
            exit 2
        }
        $msg = [IO.File]::ReadAllText($MessageFile)
        if ([string]::IsNullOrWhiteSpace($msg)) {
            Write-Err '[git-commit-helper] error: message file is empty'
            exit 2
        }

        if ($PSBoundParameters.ContainsKey('Paths') -and $Paths.Count -gt 0) {
            & git add -- @Paths
            if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
            & git commit -F $MessageFile -- @Paths
            exit $LASTEXITCODE
        } else {
            & git add -A
            if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
            & git commit -F $MessageFile
            exit $LASTEXITCODE
        }
    } catch {
        Write-Err $_.Exception.Message
        exit 1
    }
}

try {
    $gitDir = (& git rev-parse --git-dir 2>&1 | Out-String).Trim()
    if ($LASTEXITCODE -ne 0) { Write-Err $gitDir; exit 1 }
    $branch = (& git branch --show-current).Trim()
    if ([string]::IsNullOrWhiteSpace($branch)) { $branch = '(detached)' }
    & git rev-parse -q --verify HEAD > $null 2>&1
    $initialCommit = if ($LASTEXITCODE -ne 0) { 'yes' } else { 'no' }
    $mergeInProgress = if (Test-Path -LiteralPath (Join-Path $gitDir 'MERGE_HEAD')) { 'yes' } else { 'no' }

    $cachedStat = Get-NumStatMap @('--cached')
    $workStat = Get-NumStatMap @()

    $staged = New-Object System.Collections.Generic.List[string]
    $unstaged = New-Object System.Collections.Generic.List[string]
    $untracked = New-Object System.Collections.Generic.List[string]

    $totalAdd = 0
    $totalDel = 0
    foreach ($s in @($cachedStat.Values) + @($workStat.Values)) {
        if ($s.Add -ne '-') {
            $totalAdd += [int]$s.Add
            $totalDel += [int]$s.Del
        }
    }

    $lines = & git status --porcelain=v1
    $totalFiles = 0
    foreach ($raw in $lines) {
        if ($raw.Length -lt 3) { continue }
        $xy = $raw.Substring(0, 2)
        $path = $raw.Substring(3)
        $totalFiles++
        $lookup = $path
        if ($path -match ' -> ') { $lookup = ($path -split ' -> ')[-1] }
        $stat = $null
        if ($cachedStat.ContainsKey($lookup)) { $stat = $cachedStat[$lookup] }
        elseif ($workStat.ContainsKey($lookup)) { $stat = $workStat[$lookup] }
        $formatted = $xy + ' ' + $path + (Format-Stat $stat)
        if ($xy -eq '??') { $untracked.Add($formatted) }
        else {
            if ($xy[0] -ne ' ') { $staged.Add($formatted) }
            if ($xy[1] -ne ' ') { $unstaged.Add($formatted) }
        }
    }

    Write-Output ('[git-commit-helper] branch: ' + $branch)
    Write-Output ('[git-commit-helper] initial-commit: ' + $initialCommit)
    Write-Output ('[git-commit-helper] merge-in-progress: ' + $mergeInProgress)
    Write-Output '[git-commit-helper] staged:'
    foreach ($line in $staged) { Write-Output ('[git-commit-helper]   ' + $line) }
    Write-Output '[git-commit-helper] unstaged:'
    foreach ($line in $unstaged) { Write-Output ('[git-commit-helper]   ' + $line) }
    Write-Output '[git-commit-helper] untracked:'
    foreach ($line in $untracked) { Write-Output ('[git-commit-helper]   ' + $line) }
    Write-Output ('[git-commit-helper] total: ' + $totalFiles + ' files, +' + $totalAdd + '/-' + $totalDel)
    exit 0
} catch {
    Write-Err $_.Exception.Message
    exit 1
}
