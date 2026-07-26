# Flight Search Automation - MAO to CNF
# Executes at 09:00 and 15:00 daily
# Searches for one-way flights Manaus to Belo Horizonte (Confins)
# Criteria: Aug 7-14, max 1 stop, max 7h travel, arrival 8-16h, max R$1000

param(
    [string]$OutputFile = "$env:TEMP\flight-results.json"
)

$results = @()
$dateRange = @("2026-08-07","2026-08-08","2026-08-09","2026-08-10","2026-08-11","2026-08-12","2026-08-13","2026-08-14")
$userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

function Try-GoogleFlights {
    Write-Host "Tentando Google Flights..."
    $agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    try {
        $url = "https://www.google.com/travel/flights?q=flights+from+MAO+to+CNF+on+2026-08-07+oneway&curr=BRL&hl=pt-BR"
        $response = Invoke-WebRequest -Uri $url -UserAgent $agent -UseBasicParsing -TimeoutSec 15
        return @{ source = "Google Flights"; status = "loaded"; length = $response.Content.Length }
    } catch {
        return @{ source = "Google Flights"; status = "error"; error = $_.Exception.Message }
    }
}

function Try-Skyscanner {
    Write-Host "Tentando SkyScanner..."
    try {
        $url = "https://www.skyscanner.com.br/transporte/passagens-aereas/mao/cnf/?adultsv2=1&cabinclass=economy&currency=BRL&ref=home&rtn=0"
        $response = Invoke-WebRequest -Uri $url -UserAgent $userAgent -UseBasicParsing -TimeoutSec 15
        return @{ source = "SkyScanner"; status = "loaded"; length = $response.Content.Length }
    } catch {
        return @{ source = "SkyScanner"; status = "error"; error = $_.Exception.Message }
    }
}

function Try-Latam {
    Write-Host "Tentando LATAM..."
    try {
        $url = "https://www.latamairlines.com/br/pt"
        $response = Invoke-WebRequest -Uri $url -UserAgent $userAgent -UseBasicParsing -TimeoutSec 15
        return @{ source = "LATAM"; status = "loaded"; length = $response.Content.Length }
    } catch {
        return @{ source = "LATAM"; status = "error"; error = $_.Exception.Message }
    }
}

function Try-Azul {
    Write-Host "Tentando Azul..."
    try {
        $url = "https://www.voeazul.com.br/"
        $response = Invoke-WebRequest -Uri $url -UserAgent $userAgent -UseBasicParsing -TimeoutSec 15
        return @{ source = "Azul"; status = "loaded"; length = $response.Content.Length }
    } catch {
        return @{ source = "Azul"; status = "error"; error = $_.Exception.Message }
    }
}

# Run all scanners
Write-Host "=== Flight Search: MAO to CNF ===" -ForegroundColor Cyan
$timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
Write-Host "Data: $timestamp"

$results += Try-GoogleFlights
$results += Try-Skyscanner
$results += Try-Latam
$results += Try-Azul

# Save JSON results
$results | ConvertTo-Json -Depth 3 | Out-File -FilePath $OutputFile -Encoding UTF8

# Build summary
$summaryLines = @()
$summaryLines += "=== BUSCA DE PASSAGENS AEREAS ==="
$summaryLines += "Rota: Manaus (MAO) > Belo Horizonte (CNF)"
$summaryLines += "Periodo: 7 a 14 de Agosto de 2026"
$summaryLines += "Tipo: Somente ida"
$summaryLines += "Data/Hora: $(Get-Date -Format 'dd/MM/yyyy HH:mm')"
$summaryLines += ""

$summaryLines += "Resultados das fontes:"
foreach ($r in $results) {
    $line = "- $($r.source): $($r.status)"
    if ($r.error) { $line += " | $($r.error)" }
    if ($r.length) { $line += " (tamanho: $($r.length) bytes)" }
    $summaryLines += $line
}
$summaryLines += ""
$summaryLines += "Legenda:"
$summaryLines += "- loaded: Pagina carregada (pode ter JS bloqueando dados)"
$summaryLines += "- error: Falha na conexao ou bloqueio"
$summaryLines += ""
$summaryLines += "Nota: Todos os sites de passagens usam JavaScript."
$summaryLines += "O acesso automatizado e limitado sem browser grafico."

$summary = $summaryLines -join "`r`n"
$summaryFile = $OutputFile -replace '\.json$', '-summary.txt'
$summary | Out-File -FilePath $summaryFile -Encoding UTF8
Write-Host "`n$summary"
Write-Host "`n=== FIM ===" -ForegroundColor Cyan
