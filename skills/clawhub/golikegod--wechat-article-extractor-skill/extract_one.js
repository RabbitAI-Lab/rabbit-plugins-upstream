const {extract} = require('./scripts/extract.js');

(async () => {
  try {
    const result = await extract('https://mp.weixin.qq.com/s/VSCJD-1ACSP7NWoV_CI2_Q');
    console.log(JSON.stringify(result, null, 2));
  } catch (e) {
    console.error('ERROR:', e.message);
    process.exit(1);
  }
})();
