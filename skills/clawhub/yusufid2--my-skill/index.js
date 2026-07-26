#!/usr/bin/env node

const fs = require("fs");
const axios = require("axios");

const TRADE_FILE = "./trade.json";
const HISTORY_FILE = "./history.json";
const PRICE_FILE = "./prices.json";

function load(file, fallback) {
  try {
    return JSON.parse(fs.readFileSync(file));
  } catch {
    return fallback;
  }
}

function save(file, data) {
  fs.writeFileSync(file, JSON.stringify(data, null, 2));
}
function addHistory(symbol, entry, exit, pnl) {
  const history = load(HISTORY_FILE, []);

  history.push({
    time: new Date().toISOString(),
    symbol,
    entry,
    exit,
    pnl
  });

  save(HISTORY_FILE, history);
}
async function getPrice(symbol) {
  const res = await axios.get(
    `https://api.binance.com/api/v3/ticker/price?symbol=${symbol}USDT`
  );
  return parseFloat(res.data.price);
}

function getSignal(symbol, price) {

  let prices = load(PRICE_FILE, {});

  let last = prices[symbol];

  prices[symbol] = price;

  save(PRICE_FILE, prices);

  if (!last) return "HOLD";

  if (price > last) return "BUY";

  if (price < last) return "SELL";

  return "HOLD";
}

async function main() {

  const cmd = process.argv[2];
 const symbol = (process.argv[3] || "BTC").toUpperCase();
  let accounts = load(TRADE_FILE, {});

  if (!accounts[symbol]) {
    accounts[symbol] = {
      balance: 1000,
      position: null
    };
  }

  let acc = accounts[symbol];

  if (cmd === "price") {
    const price = await getPrice(symbol);
    console.log({ symbol, price });
    return;
  }

  if (cmd === "signal") {
    const price = await getPrice(symbol);
    const signal = getSignal(symbol, price);

    console.log({
      symbol,
      price,
      signal
    });

    return;
  }

  if (cmd === "status") {
    console.log(accounts);
    return;
  }

  if (cmd === "trade") {

    const price = await getPrice(symbol);

    const signal =
      getSignal(symbol, price);

    console.log("AI:", signal);

    if (signal === "BUY" && !acc.position) {

      acc.position = {
        entry: price
      };

      console.log("✅ BUY", symbol, price);
    }

    else if (signal === "SELL" && acc.position) {

      const pnl =
        price - acc.position.entry;

      acc.balance += pnl;

addHistory(
  symbol,
  acc.position.entry,
  price,
  pnl
);

acc.position = null;

      console.log("💰 CLOSE", symbol);
      console.log("PNL:", pnl);
    }

    accounts[symbol] = acc;

    save(TRADE_FILE, accounts);

    console.log(acc);

    return;
  }
}

main();

