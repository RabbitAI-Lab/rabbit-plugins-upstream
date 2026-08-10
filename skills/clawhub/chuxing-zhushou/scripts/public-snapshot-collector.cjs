const fs = require('fs');

function finite(value) {
  const n = Number(String(value ?? '').replace(/[￥¥,]/g, '').trim());
  return Number.isFinite(n) && n > 0 ? n : null;
}

function percentile(values, ratio) {
  const sorted = values.filter(Number.isFinite).sort((a, b) => a - b);
  if (!sorted.length) return null;
  const pos = (sorted.length - 1) * ratio;
  const lo = Math.floor(pos);
  const hi = Math.ceil(pos);
  return Number((sorted[lo] + (sorted[hi] - sorted[lo]) * (pos - lo)).toFixed(2));
}

function aggregatePublicPrices(input) {
  const prices = (input.prices || []).map(finite).filter(Boolean);
  if (!prices.length) {
    return {
      routeKey: `${input.from || ''}-${input.to || ''}`,
      from: input.from || '',
      to: input.to || '',
      flightDate: input.flightDate || '',
      checkedAt: input.checkedAt || new Date().toISOString(),
      sampleCount: 0,
      validPriceCount: 0,
      lowestPrice: null,
      highestPrice: null,
      averagePrice: null,
      medianPrice: null,
      p25: null,
      p75: null,
      platform: input.platform || '',
      sourceType: 'public_page',
      dataType: 'public_reference',
      parseStatus: 'empty'
    };
  }

  const direct = (input.options || []).filter(x => !x.isTransfer && finite(x.price) !== null).map(x => finite(x.price));
  const transfer = (input.options || []).filter(x => x.isTransfer && finite(x.price) !== null).map(x => finite(x.price));
  const average = prices.reduce((sum, n) => sum + n, 0) / prices.length;
  return {
    routeKey: `${input.from || ''}-${input.to || ''}`,
    from: input.from || '',
    to: input.to || '',
    flightDate: input.flightDate || '',
    checkedAt: input.checkedAt || new Date().toISOString(),
    daysBeforeDeparture: Number.isFinite(Number(input.daysBeforeDeparture)) ? Number(input.daysBeforeDeparture) : null,
    sampleCount: prices.length,
    validPriceCount: prices.length,
    lowestPrice: Math.min(...prices),
    highestPrice: Math.max(...prices),
    averagePrice: Number(average.toFixed(2)),
    medianPrice: percentile(prices, 0.5),
    p25: percentile(prices, 0.25),
    p75: percentile(prices, 0.75),
    directLowestPrice: direct.length ? Math.min(...direct) : null,
    transferLowestPrice: transfer.length ? Math.min(...transfer) : null,
    platform: input.platform || '',
    sourceType: 'public_page',
    dataType: 'public_reference',
    sourceUrl: input.sourceUrl || '',
    parseStatus: 'ok'
  };
}

function loadPublicInput(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

if (require.main === module) {
  const filePath = process.argv[2];
  if (!filePath) {
    console.error('Usage: node public-snapshot-collector.cjs <public-page-normalized.json>');
    process.exit(1);
  }
  const input = loadPublicInput(filePath);
  console.log(JSON.stringify(aggregatePublicPrices(input), null, 2));
}

module.exports = { aggregatePublicPrices, finite, percentile };
