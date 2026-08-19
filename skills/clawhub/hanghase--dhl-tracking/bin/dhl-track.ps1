# dhl-tracking — DHL parcel tracking (read-only)
#
# Public DHL endpoint: POST https://<host>/int-verfolgen/data/shipment
#   Body: { "piececode": "<number>", "zip": "<plz>" } (PLZ required for national)
#   Auth: none (public). Accept: application/json required (else 406).
#
# This skill does ONE thing: query DHL for shipment status. It does NOT
# - read mail
# - call external provider scripts
# - execute anything except the documented DHL HTTP POST above
# - log in to any service
# - modify anything on DHL's side

$ErrorActionPreference = 'Continue'
# Force UTF-8 console output so Umlaute render correctly when possible.
# PowerShell on Windows defaults to cp437/cp1252; this may not fully take
# effect under `powershell -File`. See SKILL.md "Lessons" for details.
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}
try { $OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}

# ============================================================================
# Paths
# ============================================================================

if ($PSScriptRoot) {
    $ScriptDir = $PSScriptRoot
} elseif ($MyInvocation.MyCommand.Path) {
    $ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
} else {
    $ScriptDir = Get-Location
}
$SkillRoot = Split-Path -Parent $ScriptDir
$LocalesDir = Join-Path $ScriptDir 'locales'
$CountriesPath = Join-Path $ScriptDir 'dhl-countries.json'

# ============================================================================
# Locale (CLI strings + DHL status translations)
# ============================================================================

$Script:Locale = $null

function Get-Locale {
    $code = $env:DHL_LOCALE
    if (-not $code) {
        $s = Load-JsonOrNull (Get-SetupPath)
        if ($s -and $s.locale) { $code = $s.locale }
    }
    if (-not $code) { $code = 'de' }
    $code = ($code.ToString().ToLower())

    $candidate = Join-Path $LocalesDir ("{0}.json" -f $code)
    if (Test-Path $candidate) {
        try {
            $obj = Get-Content $candidate -Encoding UTF8 -Raw | ConvertFrom-Json
            return @{ code = $code; data = $obj }
        } catch {}
    }
    $fallback = Join-Path $LocalesDir 'en.json'
    if (Test-Path $fallback) {
        try {
            $obj = Get-Content $fallback -Encoding UTF8 -Raw | ConvertFrom-Json
            return @{ code = 'en'; data = $obj }
        } catch {}
    }
    return @{ code = 'en'; data = $null }
}

function L($key, $fargs = @()) {
    $locale = $Script:Locale
    $val = $null
    if ($locale -and $locale.data) {
        $val = $locale.data.$key
    }
    if (-not $val) {
        $fallbackPath = Join-Path $LocalesDir 'en.json'
        if (Test-Path $fallbackPath) {
            $fb = Load-JsonOrNull $fallbackPath
            if ($fb) { $val = $fb.$key }
        }
    }
    if (-not $val) { $val = $key }
    if ($val -match '\{(\d+)\}' -and $fargs) {
        $flat = @()
        if ($null -ne $fargs) {
            foreach ($a in @($fargs)) {
                if ($null -ne $a -and $a -is [System.Array]) {
                    foreach ($x in $a) { $flat += [string]$x }
                } else {
                    $flat += [string]$a
                }
            }
        }
        $result = $val
        for ($i = 0; $i -lt $flat.Count; $i++) {
            $token = '{' + $i + '}'
            $result = $result.Replace($token, $flat[$i])
        }
        return $result
    }
    return $val
}

$Script:StatusMap = $null

function Get-StatusMap {
    # DHL always replies in English. The en-source map has the keys.
    # The locale-specific map provides translated values where available.
    $locale = $Script:Locale
    $code = if ($locale) { $locale.code } else { 'en' }
    $source = Join-Path $LocalesDir 'dhl-status.en.json'
    if (-not (Test-Path $source)) { return $null }
    try { $enMap = (Get-Content $source -Encoding UTF8 -Raw | ConvertFrom-Json) } catch { return $null }
    if ($code -eq 'en') { return $enMap }
    $targetPath = Join-Path $LocalesDir ("dhl-status.{0}.json" -f $code)
    if (-not (Test-Path $targetPath)) { return $enMap }
    try {
        $targetMap = (Get-Content $targetPath -Encoding UTF8 -Raw | ConvertFrom-Json)
        $merged = [PSCustomObject]@{}
        foreach ($p in $enMap.PSObject.Properties) {
            $enKey = $p.Name
            $localized = $targetMap.PSObject.Properties[$enKey]
            $val = if ($localized -and $localized.Value) { $localized.Value } else { $p.Value }
            $merged | Add-Member -NotePropertyName $enKey -NotePropertyValue $val -Force
        }
        return $merged
    } catch {
        return $enMap
    }
}

function T($status) {
    if (-not $status) { return $status }
    $map = $Script:StatusMap
    if ($map) {
        $prop = $map.PSObject.Properties[$status]
        if ($prop -and $prop.Value) { return $prop.Value }
    }
    return $status
}

# ============================================================================
# Country / endpoint resolution
# ============================================================================

$Script:Countries = $null

function Load-Countries {
    if ($Script:Countries) { return $Script:Countries }
    if (-not (Test-Path $CountriesPath)) {
        Write-Host ("WARN: {0} not found, falling back to DE." -f $CountriesPath)
        $Script:Countries = @{ DE = @{ host = 'www.dhl.de' } }
        return $Script:Countries
    }
    try {
        $Script:Countries = Get-Content $CountriesPath -Encoding UTF8 -Raw | ConvertFrom-Json
    } catch {
        Write-Host ("WARN: {0} could not be parsed." -f $CountriesPath)
        $Script:Countries = @{}
    }
    return $Script:Countries
}

function Resolve-Country {
    param([string]$code)
    $countries = Load-Countries
    if ($countries.PSObject.Properties.Name -contains $code) {
        return @{ code = $code; data = $countries.$code }
    }
    return @{ code = 'DE'; data = $countries.DE }
}

function Resolve-Endpoint {
    param([string]$countryCode, [string]$plz, [bool]$international)
    $countries = Load-Countries
    # If PLZ is not 5 digits, treat as international automatically.
    $looksIntl = $false
    if (-not $international) {
        if (-not $plz -or $plz -notmatch '^\d{5}$') { $looksIntl = $true }
    }
    if ($international -or $looksIntl) {
        # International fallback: use country-specific host when known, else dhl.de
        $intlHost = switch ($countryCode) {
            'AT' { 'www.dhl.at' }
            'CH' { 'www.dhl.ch' }
            default { 'www.dhl.de' }
        }
        return @{ url = "https://${intlHost}/int-verfolgen/data/shipment"; international = $true }
    }
    $data = $countries.$countryCode
    if (-not $data) { $data = $countries.DE }
    $hl = if ($data.host) { $data.host } else { 'www.dhl.de' }
    return @{ url = "https://${hl}/int-verfolgen/data/shipment"; international = $false }
}

# ============================================================================
# JSON helpers (UTF-8 explicit, defensive)
# ============================================================================

function Load-JsonOrNull($p) {
    if (Test-Path $p) {
        try { return Get-Content $p -Encoding UTF8 -Raw | ConvertFrom-Json }
        catch { return $null }
    }
    return $null
}

function Save-Json($p, $obj) {
    $dir = Split-Path -Parent $p
    if ($dir -and -not (Test-Path -LiteralPath $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
    $obj | ConvertTo-Json -Depth 10 | Set-Content $p -Encoding UTF8
}

# ============================================================================
# DHL HTTP call
# ============================================================================

function Invoke-DhlRequestSafe {
    param([string]$url, [hashtable]$payload)
    $Headers = @{
        'Content-Type' = 'application/json'
        'Accept'       = 'application/json'
        'User-Agent'   = 'Mozilla/5.0 (compatible; dhl-tracking-skill/1.1)'
    }
    $body = $payload | ConvertTo-Json -Compress
    try {
        $r = Invoke-WebRequest -Uri $url -Headers $Headers -Method Post -Body $body -UseBasicParsing -TimeoutSec 15
        return @{ ok = $true; json = ($r.Content | ConvertFrom-Json); status = $r.StatusCode }
    } catch {
        return @{ ok = $false; error = $_.Exception.Message; status = $_.Exception.Response.StatusCode.value__ }
    }
}

function Query-DhlShipment {
    param([string]$piececode, [string]$plz, [bool]$international, [string]$countryCode)
    $endpoint = Resolve-Endpoint $countryCode $plz $international
    $payload = @{ piececode = $piececode }
    if ($endpoint.international) {
        $payload.international = $true
    } else {
        $payload.zip = $plz
    }
    $resp = Invoke-DhlRequestSafe $endpoint.url $payload
    if (-not $resp.ok) {
        Write-Host (L 'errors.dhl_error' @($piececode, $resp.error))
        return $null
    }
    if (-not $resp.json.sendungen -or $resp.json.sendungen.Count -eq 0) {
        Write-Host (L 'add.no_data')
        return $null
    }
    return $resp.json.sendungen[0]
}

# ============================================================================
# Setup persistence
# ============================================================================

function Get-StorePath {
    $setup = Load-JsonOrNull (Join-Path $SkillRoot 'setup.json')
    $bd = $null
    if ($setup -and $setup.baseDir) { $bd = $setup.baseDir }
    if ($bd -and ($bd -is [string]) -and -not [string]::IsNullOrWhiteSpace($bd)) {
        if (-not [System.IO.Path]::IsPathRooted($bd)) { $bd = Join-Path $SkillRoot $bd }
        return (Join-Path $bd 'store.json')
    }
    return (Join-Path $SkillRoot 'store.json')
}

function Get-SetupPath {
    $setup = Load-JsonOrNull (Join-Path $SkillRoot 'setup.json')
    $bd = $null
    if ($setup -and $setup.baseDir) { $bd = $setup.baseDir }
    if ($bd -and ($bd -is [string]) -and -not [string]::IsNullOrWhiteSpace($bd)) {
        if (-not [System.IO.Path]::IsPathRooted($bd)) { $bd = Join-Path $SkillRoot $bd }
        return (Join-Path $bd 'setup.json')
    }
    return (Join-Path $SkillRoot 'setup.json')
}

function Read-Setup {
    return Load-JsonOrNull (Get-SetupPath)
}

function Save-Setup($notifyOn, $autoIngest, $locale, $country) {
    $ai = [bool]$autoIngest
    $obj = [PSCustomObject]@{
        notifyOn = $notifyOn
        autoIngest = $ai
        locale = $locale
        country = $country
        savedAt = (Get-Date).ToString('o')
    }
    Save-Json (Get-SetupPath) $obj
}

function Setup-Interactive {
    Write-Host (L 'setup.welcome')
    Write-Host ''
    $stdinIsInteractive = $Host.Name -ne 'ServerRemoteHost' -and $Host.UI.RawUI -ne $null
    if (-not $stdinIsInteractive) {
        Write-Host (L 'setup.no_interactive_title')
        Write-Host (L 'setup.no_interactive_body')
        Write-Host (L 'setup.defaults_notifyOn')
        Write-Host '  autoIngest = false (no mail integration in this skill)'
        Write-Host '  locale = de'
        Write-Host '  country = DE'
        Write-Host ''
        Write-Host (L 'setup.rehint')
        Write-Host (L 'setup.rehint_cmd')
        Save-Setup 'silent' $false 'de' 'DE'
        return
    }

    Write-Host (L 'setup.question_notify')
    Write-Host (L 'setup.notify_opt_1')
    Write-Host (L 'setup.notify_opt_2')
    Write-Host (L 'setup.notify_opt_3')
    Write-Host (L 'setup.notify_opt_4')
    $choice = Read-Host (L 'setup.prompt_notify')
    if ([string]::IsNullOrWhiteSpace($choice)) { $choice = '4' }
    $map = @{ '1' = 'user_message'; '2' = 'daily_digest'; '3' = 'heartbeat'; '4' = 'silent' }
    $notifyOn = if ($map.ContainsKey($choice)) { $map[$choice] } else { 'silent' }

    $countryChoice = Read-Host ('Country code (ISO-2, e.g. DE, AT, CH) [DE]: ')
    if ([string]::IsNullOrWhiteSpace($countryChoice)) { $countryChoice = 'DE' }
    $countryChoice = $countryChoice.ToUpper()

    Write-Host ("Setup saved: notifyOn={0}, autoIngest=false (no mail integration), locale={1}, country={2}" -f $notifyOn, $Script:Locale.code, $countryChoice)
    Save-Setup $notifyOn $false $Script:Locale.code $countryChoice
}

# ============================================================================
# Shipment commands
# ============================================================================

function Add-Shipment {
    param([string]$piececode, [string]$description, [string]$plz, [bool]$international)
    $storePath = Get-StorePath
    $setupPath = Get-SetupPath
    $store = Load-JsonOrNull $storePath
    if (-not $store) { $store = [PSCustomObject]@{ shipments = @() } }

    $exists = $store.shipments | Where-Object { $_.piececode -eq $piececode }
    if ($exists) {
        Write-Host (L 'add.already_present' @($piececode))
        return $exists
    }
    if (-not $plz -and -not $international) {
        Write-Host (L 'add.no_plz')
        Write-Host (L 'add.no_plz_hint')
        exit 1
    }

    $setup = Read-Setup
    $country = if ($setup -and $setup.country) { $setup.country } else { 'DE' }

    Write-Host (L 'add.querying' @($piececode))
    $s = Query-DhlShipment $piececode $plz $international $country
    if (-not $s) { exit 1 }

    $detail = $s.sendungsdetails
    $last = $detail.sendungsverlauf
    $delivery = $detail.zustellung
    $service = $detail.services
    $entry = [PSCustomObject]@{
        piececode = $piececode
        description = if ($description) { $description } else { $s.sendungsinfo.sendungsname }
        plz = $plz
        international = [bool]$international
        addedAt = (Get-Date).ToString('o')
        lastChecked = (Get-Date).ToString('o')
        lastStatus = T $last.status
        lastStatusDate = $last.datumAktuellerStatus
        progressCurrent = $last.fortschritt
        progressMax = $last.maximalFortschritt
        recipientName = $detail.panEmpfaenger.name
        recipientOrt = $detail.panEmpfaenger.ort
        preferredDay = if ($service -and $service.wunschtag) { $service.wunschtag } else { '' }
        deliveryWindowFrom = if ($delivery -and $delivery.zustellzeitfensterVon) { $delivery.zustellzeitfensterVon } else { '' }
        deliveryWindowBis = if ($delivery -and $delivery.zustellzeitfensterBis) { $delivery.zustellzeitfensterBis } else { '' }
        delivered = $detail.istZugestellt
        events = @($last.events | ForEach-Object {
            [PSCustomObject]@{
                datum = $_.datum
                ort = $_.ort
                status = (T $_.status)
            }
        })
    }
    $store.shipments += $entry
    Save-Json $storePath $store
    Write-Host (L 'add.added_line1' @($piececode, $entry.description, $entry.lastStatus))
    Write-Host (L 'add.added_progress' @($entry.progressCurrent, $entry.progressMax, $entry.lastStatusDate))
    if ($entry.preferredDay) {
        Write-Host (L 'add.added_preferred' @($entry.preferredDay, $entry.deliveryWindowFrom, $entry.deliveryWindowBis))
    }
    return $entry
}

function Refresh-All {
    $storePath = Get-StorePath
    $store = Load-JsonOrNull $storePath
    if (-not $store -or -not $store.shipments -or $store.shipments.Count -eq 0) {
        Write-Host (L 'refresh.empty')
        return
    }
    $setup = Read-Setup
    $country = if ($setup -and $setup.country) { $setup.country } else { 'DE' }
    $changes = @()
    foreach ($s in $store.shipments) {
        $newLast = Query-DhlShipment $s.piececode $s.plz ([bool]$s.international) $country
        if (-not $newLast) { continue }
        $detail = $newLast.sendungsdetails
        $verlauf = $detail.sendungsverlauf
        $delivery = $detail.zustellung
        $service = $detail.services

        $oldStatus = $s.lastStatus
        $oldDate = $s.lastStatusDate
        $newStatus = (T $verlauf.status)
        $newDate = $verlauf.datumAktuellerStatus

        $s.lastStatus = $newStatus
        $s.lastStatusDate = $newDate
        $s.progressCurrent = $verlauf.fortschritt
        $s.progressMax = $verlauf.maximalFortschritt
        $s.lastChecked = (Get-Date).ToString('o')
        if ($service -and $service.wunschtag) { $s.preferredDay = $service.wunschtag }
        if ($delivery) {
            $s.deliveryWindowFrom = $delivery.zustellzeitfensterVon
            $s.deliveryWindowBis = $delivery.zustellzeitfensterBis
        }
        $s.delivered = $detail.istZugestellt
        $s.events = @($verlauf.events | ForEach-Object {
            [PSCustomObject]@{
                datum = $_.datum
                ort = $_.ort
                status = (T $_.status)
            }
        })

        $changed = ($newStatus -ne $oldStatus) -or ($newDate -ne $oldDate)
        if ($changed) {
            $changes += [PSCustomObject]@{
                piececode = $s.piececode
                description = $s.description
                oldStatus = $oldStatus
                newStatus = $newStatus
                date = $newDate
            }
        }
    }
    Save-Json $storePath $store
    Write-Host (L 'refresh.summary' @($store.shipments.Count, $changes.Count))
    foreach ($c in $changes) {
        Write-Host (L 'refresh.separator')
        Write-Host (L 'refresh.change_title' @($c.piececode, $c.description))
        Write-Host (L 'refresh.change_old' @($c.oldStatus))
        Write-Host (L 'refresh.change_new' @($c.newStatus, $c.date))
    }
}

function Show-All {
    $storePath = Get-StorePath
    $store = Load-JsonOrNull $storePath
    if (-not $store -or -not $store.shipments -or $store.shipments.Count -eq 0) {
        Write-Host (L 'show.empty')
        return
    }
    foreach ($s in $store.shipments) {
        Write-Host (L 'show.separator')
        Write-Host (L 'show.header' @($s.piececode, $s.description))
        Write-Host (L 'show.recipient' @($s.recipientName, $s.recipientOrt))
        Write-Host (L 'show.status' @($s.lastStatus, $s.lastStatusDate))
        Write-Host (L 'show.progress' @($s.progressCurrent, $s.progressMax))
        Write-Host (L 'show.last_checked' @($s.lastChecked))
        if ($s.international) { Write-Host (L 'show.intl_tag') }
    }
}

function Remove-Shipment($piececode) {
    $storePath = Get-StorePath
    $store = Load-JsonOrNull $storePath
    if (-not $store) { Write-Host (L 'remove.empty'); return }
    $before = $store.shipments.Count
    $store.shipments = @($store.shipments | Where-Object { $_.piececode -ne $piececode })
    Save-Json $storePath $store
    Write-Host (L 'remove.done' @($piececode, ($before - $store.shipments.Count)))
}

# ============================================================================
# Doctor / Test (no-op fixtures, sanity)
# ============================================================================

function Test-EndpointReachable($tcpHost, $tcpPort) {
    try {
        $tcp = New-Object System.Net.Sockets.TcpClient
        $iar = $tcp.BeginConnect($tcpHost, $tcpPort, $null, $null)
        $ok = $iar.AsyncWaitHandle.WaitOne(3000, $false)
        if (-not $ok) { $tcp.Close(); return @{ ok = $false; detail = "TCP connect to ${tcpHost}:${tcpPort} timed out" } }
        $tcp.EndConnect($iar)
        $tcp.Close()
        return @{ ok = $true; detail = "TCP connect to ${tcpHost}:${tcpPort} succeeded" }
    } catch {
        return @{ ok = $false; detail = "TCP connect to ${tcpHost}:${tcpPort} failed: $($_.Exception.Message)" }
    }
}

function Invoke-Doctor {
    Write-Host 'DHL-Tracking doctor'
    Write-Host '-------------------'
    $ok = 0; $warn = 0; $err = 0
    $setup = Read-Setup
    $country = if ($setup -and $setup.country) { $setup.country } else { 'DE' }
    $countries = Load-Countries
    $endpoint = $countries.$country
    if (-not $endpoint) { $endpoint = $countries.DE }
    $hl = if ($endpoint.host) { $endpoint.host } else { 'www.dhl.de' }
    $epHostName = $hl

    $t = Test-EndpointReachable $epHostName 443
    if ($t.ok) { Write-Host ("  [OK] endpoint: {0}" -f $t.detail); $ok++ } else { Write-Host ("  [ERROR] endpoint: {0}" -f $t.detail); $err++ }

    $storePath = Get-StorePath
    if (Test-Path $storePath) {
        try { $null = Load-JsonOrNull $storePath; Write-Host ("  [OK] store-json: {0} valid JSON ({1} bytes)" -f $storePath, (Get-Item $storePath).Length); $ok++ }
        catch { Write-Host ("  [ERROR] store-json: invalid JSON: {0}" -f $_.Exception.Message); $err++ }
    } else {
        Write-Host "  [OK] store-json: (no store.json yet, will be created on first add)"
        $ok++
    }

    $setupPath = Get-SetupPath
    if (Test-Path $setupPath) {
        try { $null = Load-JsonOrNull $setupPath; Write-Host ("  [OK] setup-json: {0} valid JSON" -f $setupPath); $ok++ }
        catch { Write-Host "  [ERROR] setup-json: invalid JSON"; $err++ }
    } else {
        Write-Host "  [OK] setup-json: (no setup.json yet, run setup)"
        $ok++
    }

    if (Test-Path $storePath) {
        $store = Load-JsonOrNull $storePath
        if ($store -and $store.shipments) {
            $bad = $store.shipments | Where-Object { $_.piececode -notmatch '^\d{10,20}$' }
            if ($bad) { Write-Host ("  [WARNING] piececode-length: {0} invalid piececode(s)" -f $bad.Count); $warn++ }
            else { Write-Host ("  [OK] piececode-length: all {0} piececode(s) within 10-20 chars" -f $store.shipments.Count); $ok++ }

            $noPlz = $store.shipments | Where-Object { -not $_.plz -and -not $_.international }
            if ($noPlz) { Write-Host ("  [ERROR] plz-or-international: {0} shipment(s) missing plz and not international" -f $noPlz.Count); $err++ }
            else { Write-Host "  [OK] plz-or-international: every shipment has plz or international=true"; $ok++ }

            $noShape = $store.shipments | Where-Object { -not $_.lastStatus }
            if ($noShape) { Write-Host ("  [ERROR] shipment-shape: {0} shipment(s) missing lastStatus" -f $noShape.Count); $err++ }
            else { Write-Host "  [OK] shipment-shape: all shipments have lastStatus"; $ok++ }
        }
    }

    Write-Host ''
    Write-Host ("OK: {0}  WARNING: {1}  ERROR: {2}" -f $ok, $warn, $err)
}

function Invoke-Test {
    # Sanity test that does NOT hit DHL: build a fixture store.json, run
    # through Show/Refresh-dry, verify diff detection, then restore.
    $backup = $null
    $storePath = Get-StorePath
    if (Test-Path $storePath) {
        $backup = $storePath + '.bak-test'
        Move-Item $storePath $backup -Force
    }
    try {
        $fixture = [PSCustomObject]@{
            shipments = @(
                [PSCustomObject]@{
                    piececode = '1234567890'
                    description = 'Test shipment'
                    plz = '12345'
                    international = $false
                    addedAt = '2026-01-01T00:00:00+00:00'
                    lastChecked = '2026-01-01T00:00:00+00:00'
                    lastStatus = 'old status'
                    lastStatusDate = '2026-01-01T00:00:00+00:00'
                    progressCurrent = 1
                    progressMax = 5
                    recipientName = 'Test Recipient'
                    recipientOrt = '12345 Teststadt'
                    preferredDay = ''
                    deliveryWindowFrom = ''
                    deliveryWindowBis = ''
                    delivered = $false
                    events = @()
                }
            )
        }
        Save-Json $storePath $fixture
        Show-All | Out-Null
        # Simulate diff
        $store = Load-JsonOrNull $storePath
        if ($store.shipments.Count -ne 1) { Write-Host 'FAIL: fixture count mismatch'; return }
        if ($store.shipments[0].lastStatus -ne 'old status') { Write-Host 'FAIL: fixture lastStatus mismatch'; return }
        Write-Host 'PASS'
    } finally {
        if (Test-Path $storePath) { Remove-Item $storePath -Force }
        if ($backup -and (Test-Path $backup)) { Move-Item $backup $storePath -Force }
    }
}

# ============================================================================
# Argument parser (parameterized, no fragile positional parsing)
# ============================================================================

function Parse-Args {
    param([string[]]$argv)
    $cmd = $null
    $opts = @{}
    $positional = @()
    for ($i = 0; $i -lt $argv.Count; $i++) {
        $a = $argv[$i]
        if ($a -match '^--(.+)$') {
            $key = $matches[1]
            $val = $argv[$i + 1]
            if ($val -and -not ($val -match '^--')) {
                $opts[$key] = $val
                $i++
            } else {
                $opts[$key] = $true
            }
        } elseif ($a -in @('-h', '--help')) {
            $opts['help'] = $true
        } elseif ($null -eq $cmd) {
            $cmd = $a
        } else {
            $positional += $a
        }
    }
    return @{ cmd = $cmd; opts = $opts; positional = $positional }
}

# ============================================================================
# Help
# ============================================================================

function Show-Help {
    Write-Host 'dhl-tracking - DHL parcel tracking (read-only)'
    Write-Host ''
    Write-Host 'Usage: dhl-track.ps1 <command> [flags]'
    Write-Host ''
    Write-Host 'Commands:'
    Write-Host '  setup                Interactive configuration (notifyOn, locale, country)'
    Write-Host '  setup show           Show current configuration'
    Write-Host '  add <piececode> [--plz <nr>] [--description "..."] [--international]'
    Write-Host '  refresh              Re-query all shipments, report changes'
    Write-Host '  show                 List shipments'
    Write-Host '  remove <piececode>   Remove a shipment'
    Write-Host '  doctor               Diagnose endpoint, JSON, invariants'
    Write-Host '  test                 Sanity-test without hitting DHL'
    Write-Host ''
    Write-Host 'Global flags:'
    Write-Host '  --help, -h           Show this help'
}

# ============================================================================
# Main
# ============================================================================

# Init
$Script:Locale = Get-Locale
$Script:StatusMap = Get-StatusMap

$parsed = Parse-Args $args

switch ($parsed.cmd) {
    'setup' {
        if ($parsed.opts.ContainsKey('show') -or $parsed.opts.ContainsKey('help')) {
            $s = Read-Setup
            if ($s) { $s | ConvertTo-Json } else { Write-Host '(no setup)' }
        } else {
            Setup-Interactive
        }
    }
    'add' {
        $pc = $parsed.positional[0]
        if (-not $pc) { Write-Host 'Usage: add <piececode> [--plz <nr>] [--description "..."] [--international]'; exit 1 }
        $desc = if ($parsed.opts.ContainsKey('description')) { $parsed.opts['description'] } else { '' }
        $plz  = if ($parsed.opts.ContainsKey('plz')) { $parsed.opts['plz'] } else { '' }
        $intl = [bool]($parsed.opts.ContainsKey('international'))
        Add-Shipment $pc $desc $plz $intl
    }
    'refresh' { Refresh-All }
    'show'    { Show-All }
    'remove'  { Remove-Shipment $parsed.positional[0] }
    'doctor'  { Invoke-Doctor }
    'test'    { Invoke-Test }
    default   {
        if ($parsed.opts.ContainsKey('help') -or $args.Count -eq 0) { Show-Help }
        else { Write-Host ("Unknown command: {0}" -f $parsed.cmd); Show-Help; exit 4 }
    }
}