## Description: <br>
Fetches next-hour predicted price for BTC/ETH from external prediction API. Supports BTCUSDT and ETHUSDT symbols only. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stevenho1394](https://clawhub.ai/user/stevenho1394) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to request a quick next-hour BTCUSDT or ETHUSDT price prediction from an external service and receive a normalized result with current price, predicted price, and direction. The output is informational only and is not financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts external services for BTC/ETH prediction and current price data. <br>
Mitigation: Install and run it only where calls to myfastapi.zeabur.app and CoinGecko are acceptable. <br>
Risk: The prediction source is opaque and may be inaccurate or unavailable. <br>
Mitigation: Treat outputs as informational only, not as financial advice or an automated trading signal. <br>
Risk: The skill stores a local timezone preference under the user's home configuration directory. <br>
Mitigation: Use an explicit timezone parameter when possible and review the local configuration behavior before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/stevenho1394/skills/crypto-price-prediction) <br>
- [Publisher profile](https://clawhub.ai/user/stevenho1394) <br>
- [External prediction API endpoint](https://myfastapi.zeabur.app/v1/demo/predictions/next_hour) <br>
- [CoinGecko simple price API](https://api.coingecko.com/api/v3/simple/price) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON] <br>
**Output Format:** [JSON object with timestamp, symbol, horizonHours, currentPrice, predictedPrice, and predictedDirection; the Python script may also print a short plain-text summary.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports BTCUSDT and ETHUSDT only; the prediction horizon is fixed at one hour.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
