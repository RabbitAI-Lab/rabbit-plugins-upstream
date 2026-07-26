## Description: <br>
Download, process, and backtest ByBit derivatives historical order book data using Selenium-based downloads, order book snapshot processing, and built-in trading strategy backtests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davidm413](https://clawhub.ai/user/davidm413) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and quantitative trading practitioners use this skill to download ByBit order book snapshots, convert them into analysis-ready Parquet data, and generate strategy backtest reports. It is intended for historical market-data analysis rather than live trading execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release security summary flags Selenium automation that reportedly bypasses Cloudflare protections. <br>
Mitigation: Prefer Bybit's official APIs or documented data exports, confirm permitted access before automation, and use manual downloads when browser automation is blocked. <br>
Risk: The release security guidance flags system-level Python installation advice using --break-system-packages. <br>
Mitigation: Install dependencies in a virtual environment or other isolated Python environment instead of modifying the system Python environment. <br>
Risk: The artifact writes downloaded data, processed Parquet files, and reports to local output directories. <br>
Mitigation: Run the scripts in a dedicated working directory and set explicit input, output, data, and report paths before execution. <br>


## Reference(s): <br>
- [ByBit Order Book Data Reference](artifact/bybit_data_format.md) <br>
- [Strategy Reference](artifact/strategies.md) <br>
- [Bybit Derivatives History Data](https://www.bybit.com/derivatives/en/history-data) <br>
- [Bybit Public Trading Data Pattern](https://public.bybit.com/trading/{SYMBOL}/{SYMBOL}{YYYY-MM-DD}.csv.gz) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, files, markdown, JSON] <br>
**Output Format:** [Markdown guidance with inline bash commands; generated artifacts include ZIP downloads, Parquet datasets, JSON reports, and Markdown reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include PnL, Sharpe ratio, win rate, drawdown, equity curves, and strategy comparisons.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
