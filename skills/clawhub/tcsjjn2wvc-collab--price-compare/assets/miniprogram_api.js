/**
 * 一券省 · 全网比价 & 外卖比价 小程序集成模块 v2.0
 *
 * ============================================
 * 架构说明（安全第一）
 * ============================================
 * 本文件为小程序端 API 封装层。
 * ⚠️ 所有 API 密钥存储在后端服务器，小程序端不存储任何密钥！
 * 小程序 → 后端中转 → 各平台API
 *
 * 集成方式：
 * 1. 将本文件放入小程序项目 utils/api.js
 * 2. 在 app.js 引入：const API = require('./utils/api')
 * 3. 在本文件顶部修改 API_BASE 为你的后端地址
 * 4. 在页面中调用 API.compareAll() 等方法
 */

// ============ 后端配置 ============
const API_BASE = 'https://mini.juanshenghui.com/api'

// 默认城市ID（外卖用）
const DEFAULT_CITY_ID = 1

// 请求超时（毫秒）
const TIMEOUT = 15000

// ============ 核心请求层 ============

/**
 * 统一请求封装（带重试和缓存）
 */
function request(options) {
  return new Promise((resolve, reject) => {
    const retryCount = options.retry || 1
    let attempts = 0

    function doRequest() {
      attempts++
      const startTime = Date.now()

      wx.request({
        url: options.url,
        method: options.method || 'GET',
        data: options.data || {},
        header: {
          'content-type': 'application/json',
          ...options.header,
        },
        timeout: options.timeout || TIMEOUT,
        success(res) {
          const elapsed = Date.now() - startTime

          // HTTP 状态检查
          if (res.statusCode !== 200) {
            if (attempts < retryCount) {
              console.warn(`[API] ${options.url} 重试 ${attempts}/${retryCount}`)
              setTimeout(doRequest, 1000 * attempts)
              return
            }
            reject(new Error(`服务器错误 (${res.statusCode})`))
            return
          }

          // 业务状态检查
          const data = res.data
          if (data && data.code === 0) {
            resolve(data.data)
          } else {
            reject(new Error(data?.msg || data?.message || '请求失败'))
          }
        },
        fail(err) {
          if (attempts < retryCount) {
            console.warn(`[API] ${options.url} 网络重试 ${attempts}/${retryCount}`)
            setTimeout(doRequest, 1000 * attempts)
            return
          }
          // 网络错误友好提示
          if (err.errMsg && err.errMsg.includes('timeout')) {
            reject(new Error('网络超时，请检查网络后重试'))
          } else if (err.errMsg && err.errMsg.includes('fail')) {
            reject(new Error('网络连接失败，请检查网络'))
          } else {
            reject(err)
          }
        },
      })
    }

    doRequest()
  })
}

// ============ 工具函数 ============

/**
 * 价格格式化（保留两位小数）
 */
function formatPrice(price) {
  const num = parseFloat(price)
  if (isNaN(num)) return '0.00'
  return num.toFixed(2)
}

/**
 * 计算节省金额
 */
function calcSaved(original, current) {
  const orig = parseFloat(original) || 0
  const curr = parseFloat(current) || 0
  return Math.max(0, orig - curr).toFixed(2)
}

/**
 * 构建分享参数
 */
function buildShareParams(data) {
  return {
    title: `比价结果: ${data.keyword || '商品'}`,
    path: `/pages/index/index?from=share`,
    imageUrl: data.image || '',
  }
}

// ============ 比价 API ============

/**
 * 【全网比价】查询所有平台
 *
 * @param {string}  keyword   - 搜索关键词
 * @param {object}  options   - 可选参数
 * @param {number}  options.cityId     - 城市ID（外卖用，默认1）
 * @param {number}  options.page       - 页码（默认1）
 * @param {number}  options.pageSize   - 每页数量（默认20）
 * @param {array}   options.platforms  - 指定平台 ['jd','taobao','meituan','eleme']
 * @returns {Promise<object>} 比价结果 { keyword, count, results, best, coupons }
 *
 * @example
 * const result = await API.compareAll('手机壳')
 * console.log(result.best) // 最便宜的商品
 */
function compareAll(keyword, options = {}) {
  if (!keyword || !keyword.trim()) {
    return Promise.reject(new Error('请输入搜索关键词'))
  }

  const params = {
    keyword: keyword.trim(),
    city_id: options.cityId || DEFAULT_CITY_ID,
    page: options.page || 1,
    page_size: Math.min(options.pageSize || 20, 50),
  }

  if (options.platforms) {
    params.platforms = options.platforms.join(',')
  }

  return request({
    url: `${API_BASE}/compare/all`,
    method: 'POST',
    data: params,
    retry: 2,
  }).then(formatCompareResult)
}

/**
 * 【外卖比价】美团 vs 饿了么
 *
 * @param {string}  keyword - 商家名或菜品名
 * @param {number}  cityId  - 城市ID
 * @returns {Promise<object>} { keyword, meituan: [], eleme: [], best }
 *
 * @example
 * const result = await API.compareWaimai('黄焖鸡', 1)
 * // result.meituan - 美团结果
 * // result.eleme   - 饿了么结果
 * // result.best    - 综合最优
 */
function compareWaimai(keyword, cityId = DEFAULT_CITY_ID) {
  if (!keyword || !keyword.trim()) {
    return Promise.reject(new Error('请输入搜索关键词'))
  }

  return request({
    url: `${API_BASE}/compare/waimai`,
    method: 'POST',
    data: {
      keyword: keyword.trim(),
      city_id: cityId,
    },
    retry: 2,
  }).then(formatWaimaiResult)
}

/**
 * 【搜索建议】输入联想
 *
 * @param {string} keyword - 部分关键词
 * @returns {Promise<string[]>} 建议词列表
 */
function searchSuggest(keyword) {
  if (!keyword || keyword.length < 1) {
    return Promise.resolve([])
  }

  return request({
    url: `${API_BASE}/search/suggest`,
    method: 'GET',
    data: { keyword: keyword.trim(), limit: 10 },
  }).then(data => data.suggestions || [])
}

// ============ 红包/优惠券 API ============

/**
 * 【获取可领红包】各平台当前可领红包
 *
 * @param {string|string[]} platforms - 指定平台 'meituan'/'eleme'/'jd'/'taobao' 或 'all'
 * @returns {Promise<object>} 各平台红包列表
 *
 * @example
 * const coupons = await API.getAvailableCoupons('all')
 * // coupons.meituan.count     - 美团红包数量
 * // coupons.meituan.maxAmount - 美团最大红包金额
 * // coupons.meituan.coupons   - 红包列表
 */
function getAvailableCoupons(platforms = 'all') {
  const list = platforms === 'all'
    ? 'meituan,eleme,jd,taobao'
    : Array.isArray(platforms) ? platforms.join(',') : platforms

  return request({
    url: `${API_BASE}/coupon/available`,
    method: 'GET',
    data: { platforms: list },
  }).then(formatCouponResult)
}

/**
 * 【领取红包】
 *
 * @param {string} platform - 平台 'meituan'/'eleme'/'jd'/'taobao'
 * @param {string} couponId - 红包ID
 * @returns {Promise<object>} { status, link, message }
 *
 * @example
 * const result = await API.claimCoupon('meituan', 'abc123')
 * // result.link - 红包使用链接
 */
function claimCoupon(platform, couponId) {
  if (!platform || !couponId) {
    return Promise.reject(new Error('参数不完整'))
  }

  return request({
    url: `${API_BASE}/coupon/claim`,
    method: 'POST',
    data: { platform, coupon_id: couponId },
  })
}

/**
 * 【获取红包历史】用户已领红包记录
 *
 * @param {number} page - 页码
 * @returns {Promise<object>} { list: [], total: 0 }
 */
function getCouponHistory(page = 1) {
  return request({
    url: `${API_BASE}/coupon/history`,
    method: 'GET',
    data: { page, page_size: 20 },
  })
}

// ============ 历史记录 API ============

/**
 * 【比价历史】用户最近的比价搜索
 */
function getSearchHistory(page = 1) {
  return request({
    url: `${API_BASE}/search/history`,
    method: 'GET',
    data: { page, page_size: 20 },
  })
}

/**
 * 【清空搜索历史】
 */
function clearSearchHistory() {
  return request({
    url: `${API_BASE}/search/history`,
    method: 'DELETE',
  })
}

// ============ 结果格式化 ============

function formatCompareResult(data) {
  // data 来自后端已聚合的结果
  const results = (data.results || []).map((item, idx) => ({
    rank: idx + 1,
    platform: item.platform || '未知',
    platformIcon: getPlatformIcon(item.platform),
    title: item.title || '',
    shop: item.shop || '',
    price: formatPrice(item.price || 0),
    priceRaw: parseFloat(item.price || 0),
    couponAmount: formatPrice(item.coupon_amount || item.couponAmount || 0),
    couponAmountRaw: parseFloat(item.coupon_amount || item.couponAmount || 0),
    afterPrice: formatPrice(item.after_price || item.afterPrice || item.price || 0),
    afterPriceRaw: parseFloat(item.after_price || item.afterPrice || item.price || 0),
    saved: calcSaved(item.price, item.after_price || item.afterPrice || item.price),
    url: item.url || item.link || '',
    image: item.image || item.pic || '',
    sales: item.sales || item.monthly_sales || 0,
    rating: parseFloat(item.rating || 0).toFixed(1),
    // 是否是外卖
    isWaimai: ['美团', '饿了么'].includes(item.platform),
    // 是否有红包
    hasCoupon: parseFloat(item.coupon_amount || item.couponAmount || 0) > 0,
  }))

  // 按到手价排序
  results.sort((a, b) => a.afterPriceRaw - b.afterPriceRaw)

  return {
    keyword: data.keyword || '',
    count: results.length,
    results,
    best: results[0] || null,
    // 统计
    stats: {
      platforms: [...new Set(results.map(r => r.platform))],
      totalSaved: results.reduce((sum, r) => sum + parseFloat(r.saved), 0).toFixed(2),
      withCoupon: results.filter(r => r.hasCoupon).length,
      waimai: results.filter(r => r.isWaimai).length,
    },
  }
}

function formatWaimaiResult(data) {
  const meituanItems = (data.meituan || []).slice(0, 10)
  const elemeItems = (data.eleme || []).slice(0, 10)

  function formatItem(item) {
    const price = parseFloat(item.price || item.currentPrice || 0)
    const coupon = parseFloat(item.coupon_amount || item.couponAmount || 0)
    return {
      title: item.title || item.name || '',
      shop: item.shop || item.shopName || '',
      price: formatPrice(price),
      priceRaw: price,
      couponAmount: formatPrice(coupon),
      couponAmountRaw: coupon,
      afterPrice: formatPrice(Math.max(0, price - coupon)),
      afterPriceRaw: Math.max(0, price - coupon),
      url: item.url || item.link || '',
      rating: parseFloat(item.rating || 0).toFixed(1),
      monthlySales: item.monthly_sales || item.sales || 0,
      deliveryTime: item.delivery_time || '',
      deliveryFee: formatPrice(item.delivery_fee || 0),
    }
  }

  const meituan = meituanItems.map(formatItem)
  const eleme = elemeItems.map(formatItem)

  // 综合最优
  const allItems = [...meituan, ...eleme]
  allItems.sort((a, b) => a.afterPriceRaw - b.afterPriceRaw)

  return {
    keyword: data.keyword || '',
    meituan,
    eleme,
    best: allItems[0] || null,
    // 平台对比
    comparison: {
      meituanCount: meituan.length,
      elemeCount: eleme.length,
      meituanMinPrice: meituan.length > 0 ? meituan[0].afterPrice : '--',
      elemeMinPrice: eleme.length > 0 ? eleme[0].afterPrice : '--',
    },
  }
}

function formatCouponResult(data) {
  const platformNames = {
    meituan: '美团',
    eleme: '饿了么',
    jd: '京东',
    taobao: '淘宝',
  }

  const result = {}
  let totalCoupons = 0
  let totalMaxAmount = 0

  Object.keys(platformNames).forEach(platform => {
    const platformData = data[platform] || {}
    const coupons = (platformData.coupons || platformData.list || []).map(c => ({
      id: c.id || c.coupon_id || c.batchId || '',
      name: c.name || c.title || c.couponName || '',
      amount: formatPrice(c.amount || c.discount || c.value || 0),
      amountRaw: parseFloat(c.amount || c.discount || c.value || 0),
      condition: c.condition || c.min_amount
        ? `满${c.min_amount || c.condition}可用`
        : '无门槛',
      expire: c.expire || c.endTime || c.validTime || '',
      url: c.url || c.claim_url || c.link || c.h5Link || '',
      claimed: c.claimed || false,
    }))

    const maxAmount = coupons.length > 0
      ? Math.max(...coupons.map(c => c.amountRaw))
      : 0

    result[platform] = {
      name: platformNames[platform],
      count: coupons.length,
      maxAmount: formatPrice(maxAmount),
      maxAmountRaw: maxAmount,
      coupons: coupons.slice(0, 10),
    }

    totalCoupons += coupons.length
    totalMaxAmount = Math.max(totalMaxAmount, maxAmount)
  })

  result._summary = {
    totalCoupons,
    maxAmount: formatPrice(totalMaxAmount),
  }

  return result
}

// ============ 平台图标 ============

function getPlatformIcon(platform) {
  const icons = {
    '京东': '🛒',
    '淘宝': '🛍️',
    '美团': '🍱',
    '饿了么': '🛵',
  }
  return icons[platform] || '📦'
}

// ============ 导出 ============

module.exports = {
  // 核心比价
  compareAll,
  compareWaimai,
  searchSuggest,

  // 红包
  getAvailableCoupons,
  claimCoupon,
  getCouponHistory,

  // 历史
  getSearchHistory,
  clearSearchHistory,

  // 工具
  formatPrice,
  calcSaved,
  buildShareParams,
  getPlatformIcon,

  // 配置
  API_BASE,
  DEFAULT_CITY_ID,
}
