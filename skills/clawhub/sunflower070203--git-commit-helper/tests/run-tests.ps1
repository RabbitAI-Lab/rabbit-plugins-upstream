[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = 'Stop'

$script:helper = Join-Path $PSScriptRoot '..\scripts\git-commit-helper.ps1'
$script:passed = 0
$script:failed = 0

function New-TestRepo {
    $dir = Join-Path ([IO.Path]::GetTempPath()) ('gch-test-' + [guid]::NewGuid().ToString('N'))
    New-Item -ItemType Directory -Path $dir | Out-Null
    Push-Location $dir
    git init -q
    git config user.name 'Test User'
    git config user.email 'test@example.com'
    return $dir
}

function Close-TestRepo {
    param([string]$Dir)
    Pop-Location
    Remove-Item -LiteralPath $Dir -Recurse -Force
}

function Write-FileUtf8 {
    param([string]$Path, [string]$Content)
    [IO.File]::WriteAllText($Path, $Content, (New-Object System.Text.UTF8Encoding($false)))
}

function Assert-Contains {
    param([string]$Haystack, [string]$Needle, [string]$Case)
    if ($Haystack.Contains($Needle)) {
        Write-Host ('PASS: ' + $Case) -ForegroundColor Green
        $script:passed++
    } else {
        Write-Host ('FAIL: ' + $Case) -ForegroundColor Red
        Write-Host ('  expected to contain: ' + $Needle)
        Write-Host '  actual:'
        Write-Host $Haystack
        $script:failed++
    }
}

function Assert-Equal {
    param([string]$Actual, [string]$Expected, [string]$Case)
    if ($Actual -eq $Expected) {
        Write-Host ('PASS: ' + $Case) -ForegroundColor Green
        $script:passed++
    } else {
        Write-Host ('FAIL: ' + $Case) -ForegroundColor Red
        Write-Host ('  expected: [' + $Expected + ']')
        Write-Host ('  actual:   [' + $Actual + ']')
        $script:failed++
    }
}

function Assert-ExitCode {
    param([int]$Actual, [int]$Expected, [string]$Case)
    if ($Actual -eq $Expected) {
        Write-Host ('PASS: ' + $Case) -ForegroundColor Green
        $script:passed++
    } else {
        Write-Host ('FAIL: ' + $Case) -ForegroundColor Red
        Write-Host ('  expected exit code ' + $Expected + ', got ' + $Actual)
        $script:failed++
    }
}

function Test-EmptyRepo {
    $dir = New-TestRepo
    try {
        $out = & $script:helper analyze 2>&1
        $code = $LASTEXITCODE
        $text = $out -join "`n"
        Assert-ExitCode $code 0 'empty repo: exit 0'
        Assert-Contains $text '[git-commit-helper] total: 0 files' 'empty repo: total 0 files'
        Assert-Contains $text '[git-commit-helper] initial-commit: yes' 'empty repo: initial-commit yes'
        Assert-Contains $text '[git-commit-helper] merge-in-progress: no' 'empty repo: merge flag no'
    } finally { Close-TestRepo $dir }
}

function Test-MixedChanges {
    $dir = New-TestRepo
    try {
        Write-FileUtf8 (Join-Path $dir 'base.txt') 'one'
        & git add base.txt
        & git commit -q -m 'chore: init'
        Write-FileUtf8 (Join-Path $dir 'base.txt') 'one changed'
        Write-FileUtf8 (Join-Path $dir 'staged.txt') 'two'
        & git add staged.txt
        Write-FileUtf8 (Join-Path $dir 'new.txt') 'three'
        $out = & $script:helper analyze 2>&1
        $code = $LASTEXITCODE
        $text = $out -join "`n"
        Assert-ExitCode $code 0 'mixed changes: exit 0'
        Assert-Contains $text 'A  staged.txt' 'mixed changes: staged add listed'
        Assert-Contains $text 'M base.txt' 'mixed changes: unstaged modify listed'
        Assert-Contains $text '?? new.txt' 'mixed changes: untracked listed'
        Assert-Contains $text 'total: 3 files' 'mixed changes: total 3 files'
    } finally { Close-TestRepo $dir }
}

function Test-InitialCommit {
    $dir = New-TestRepo
    try {
        Write-FileUtf8 (Join-Path $dir 'a.txt') 'x'
        & git add a.txt
        $out = & $script:helper analyze 2>&1
        $text = $out -join "`n"
        Assert-Contains $text '[git-commit-helper] initial-commit: yes' 'initial commit: detected'
        Assert-Contains $text 'A  a.txt' 'initial commit: staged file listed'
    } finally { Close-TestRepo $dir }
}

function Test-MergeInProgress {
    $dir = New-TestRepo
    try {
        $main = (& git symbolic-ref --short HEAD).Trim()
        Write-FileUtf8 (Join-Path $dir 'f.txt') 'base'
        & git add f.txt
        & git commit -q -m 'chore: base'
        & git checkout -q -b side
        Write-FileUtf8 (Join-Path $dir 'f.txt') 'side'
        & git commit -q -am 'chore: side'
        & git checkout -q $main
        Write-FileUtf8 (Join-Path $dir 'f.txt') 'master'
        & git commit -q -am 'chore: master'
        & git merge side 2>&1 | Out-Null
        $out = & $script:helper analyze 2>&1
        $text = $out -join "`n"
        Assert-Contains $text '[git-commit-helper] merge-in-progress: yes' 'merge in progress: flag detected'
    } finally { Close-TestRepo $dir }
}

Test-EmptyRepo
Test-MixedChanges
Test-InitialCommit
Test-MergeInProgress

function Test-CommitQuotedMessage {
    $dir = New-TestRepo
    try {
        Write-FileUtf8 (Join-Path $dir 'f.txt') 'x'
        & git add f.txt
        $expected = [IO.File]::ReadAllText((Join-Path $PSScriptRoot 'fixtures\expected-msg.txt'), [System.Text.Encoding]::UTF8).Trim()
        $msgFile = Join-Path $dir 'msg.txt'
        Write-FileUtf8 $msgFile $expected
        & $script:helper commit -MessageFile $msgFile 2>&1 | Out-Null
        $code = $LASTEXITCODE
        Assert-ExitCode $code 0 'quoted message: exit 0'
        $log = ((git log -1 --format=%B) -join "`n").Trim()
        Assert-Equal $log $expected 'quoted message: message preserved exactly'
        Assert-Contains $log 'feat: add "quoted" feature' 'quoted message: subject preserved'
    } finally { Close-TestRepo $dir }
}

function Test-CommitPaths {
    $dir = New-TestRepo
    try {
        Write-FileUtf8 (Join-Path $dir 'one.txt') '1'
        Write-FileUtf8 (Join-Path $dir 'two.txt') '2'
        & git add one.txt two.txt
        $msgFile = Join-Path $dir 'msg.txt'
        Write-FileUtf8 $msgFile 'chore: add one'
        & $script:helper commit -MessageFile $msgFile -Paths 'one.txt' 2>&1 | Out-Null
        $code = $LASTEXITCODE
        Assert-ExitCode $code 0 'paths subset: exit 0'
        $files = ((git diff-tree --root --no-commit-id --name-only -r HEAD) -join "`n")
        Assert-Contains $files 'one.txt' 'paths subset: only one.txt committed'
        $status = ((git status --porcelain=v1) -join "`n")
        Assert-Contains $status 'A  two.txt' 'paths subset: two.txt remains staged'
    } finally { Close-TestRepo $dir }
}

function Test-EmptyMessage {
    $dir = New-TestRepo
    try {
        Write-FileUtf8 (Join-Path $dir 'f.txt') 'x'
        & git add f.txt
        $emptyFile = Join-Path $dir 'empty.txt'
        Write-FileUtf8 $emptyFile "   "
        & $script:helper commit -MessageFile $emptyFile 2>&1 | Out-Null
        $code = $LASTEXITCODE
        Assert-ExitCode $code 2 'empty message: exit 2'
        & git rev-parse -q --verify HEAD > $null 2>&1
        Assert-ExitCode $LASTEXITCODE 1 'empty message: no commit created'
    } finally { Close-TestRepo $dir }
}

function Test-HookFailure {
    $dir = New-TestRepo
    try {
        Write-FileUtf8 (Join-Path $dir 'f.txt') 'x'
        & git add f.txt
        Write-FileUtf8 (Join-Path $dir '.git\hooks\pre-commit') 'exit 1'
        $msgFile = Join-Path $dir 'msg.txt'
        Write-FileUtf8 $msgFile 'chore: should fail'
        & $script:helper commit -MessageFile $msgFile 2>&1 | Out-Null
        $code = $LASTEXITCODE
        Assert-ExitCode $code 1 'hook failure: exit non-zero'
        & git rev-parse -q --verify HEAD > $null 2>&1
        Assert-ExitCode $LASTEXITCODE 1 'hook failure: no commit created'
    } finally { Close-TestRepo $dir }
}

Test-CommitQuotedMessage
Test-CommitPaths
Test-EmptyMessage
Test-HookFailure

Write-Host ''
Write-Host ('RESULT: ' + $script:passed + ' passed, ' + $script:failed + ' failed')
if ($script:failed -gt 0) { exit 1 } else { exit 0 }
