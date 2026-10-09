# 🌾 SelfPaid (YieldFarmSecurepay)

Zero-net-cost payments on Base Mainnet (Chain ID 8453). Send USDC to any recipient while recovering **100% of the principal + developer fee** automatically through collateral yield farming on Aave V3 and Morpho.

## 🚀 Key Features

* **100% Capital Recovery**: Principal spent on payments is fully recovered through DeFi yield.
* **Pure M2M Architecture**: Generates clean, ready-to-sign EVM transactions and EIP-5792 atomic batch calls.
* **Dynamic Yield Optimizer**: Automatically selects the highest yielding protocol between Aave V3 and Morpho.
* **Transparent Monetization**: Built-in 0.5% developer fee (min 0.1 USDC, max 50 USDC), completely recovered by the yield.
* **Non-Custodial**: No private keys ever stored or requested.

## 🌐 Hosted API (Base Mainnet)

* **Oracle Rates**: `GET https://selfpaid.cryptofolio.it/api/v1/payment/rates`
* **Calculate Quote**: `GET https://selfpaid.cryptofolio.it/api/v1/payment/quote?amount=25`
* **Build Transactions**: `POST https://selfpaid.cryptofolio.it/api/v1/payment/build`

For detailed agent integration and mathematical models, see `SKILL.md`.

## ⚠️ Risk Disclosure

DeFi protocol deposits carry inherent smart contract, oracle, and liquidity risks. Transactions on Base Mainnet are irreversible. Principal recovery estimates are dynamic and fluctuate based on market lending yields on Aave V3 and Morpho.

