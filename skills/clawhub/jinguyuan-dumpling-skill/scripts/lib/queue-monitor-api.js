'use strict';

/**
 * Queue monitoring REST client for the Skill CLI.
 *
 * Wraps the JGY backend queue endpoints (mounted at /api/v1/queue/*) via
 * jgy-api.js so that host allow-listing, timeout, and error handling stay
 * consistent with the rest of the Skill.
 *
 * All queue endpoints are public — no auth required.
 */

const { createApiClient } = require('./jgy-api');

function createQueueMonitorApi() {
  const client = createApiClient();
  const { businessApi, request } = client;

  async function queueCall(path, body) {
    const url = `${businessApi}${path}`;
    try {
      const data = await request(url, { method: 'POST', json: body ?? {} });
      return data;
    } catch (err) {
      if (err && err.code === 'HTTP_ERROR' && err.body && typeof err.body === 'object') {
        return err.body;
      }
      return {
        ok: false,
        code: err && err.code ? err.code : 'NETWORK_ERROR',
        message: '排队信息查询失败，请稍后重试。',
      };
    }
  }

  /**
   * POST /api/v1/queue/query
   * Query current queue status for a shop.
   * @param {object} params — { shopId, ... }
   */
  function queryQueue(params) {
    return queueCall('/queue/query', params);
  }

  /**
   * POST /api/v1/queue/at-time
   * Query queue status at a specific time.
   * @param {object} params — { shopId, at, ... }
   */
  function queryQueueAtTime(params) {
    return queueCall('/queue/at-time', params);
  }

  /**
   * POST /api/v1/queue/period-facts
   * Get aggregated queue facts for a time period.
   * @param {object} params — { shopId, since, until, ... }
   */
  function getPeriodFacts(params) {
    return queueCall('/queue/period-facts', params);
  }

  /**
   * POST /api/v1/queue/period-advice
   * Get visit-time advice based on queue patterns.
   * @param {object} params — { shopId, ... }
   */
  function getPeriodAdvice(params) {
    return queueCall('/queue/period-advice', params);
  }

  return { queryQueue, queryQueueAtTime, getPeriodFacts, getPeriodAdvice };
}

module.exports = { createQueueMonitorApi };
