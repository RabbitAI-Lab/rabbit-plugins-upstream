const { aggregatePublicPrices, finite } = require('./public-snapshot-collector.cjs');

function text(value) {
  return String(value ?? '').replace(/\s+/g, ' ').trim();
}

function normalizeVisibleOptions(input) {
  const options = Array.isArray(input.options) ? input.options : [];
  return options.map((item) => ({
    flightNo: text(item.flightNo),
    airlineName: text(item.airlineName),
    depTime: text(item.depTime),
    arrTime: text(item.arrTime),
    price: finite(item.price),
    isTransfer: Boolean(item.isTransfer)
  })).filter((item) => item.price !== null);
}

function normalizePublicPage(input) {
  const options = normalizeVisibleOptions(input);
  return aggregatePublicPrices({
    from: text(input.from),
    to: text(input.to),
    flightDate: text(input.flightDate),
    checkedAt: input.checkedAt,
    daysBeforeDeparture: input.daysBeforeDeparture,
    platform: text(input.platform || 'ctrip_public_page'),
    sourceUrl: text(input.sourceUrl),
    prices: options.map((item) => item.price),
    options,
    parseStatus: options.length ? 'ok' : 'empty'
  });
}

module.exports = { normalizePublicPage, normalizeVisibleOptions };
