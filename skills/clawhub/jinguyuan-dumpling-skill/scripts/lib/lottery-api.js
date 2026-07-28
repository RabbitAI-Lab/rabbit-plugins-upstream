'use strict';

/**
 * Lottery & prize REST client for the Skill CLI.
 *
 * Built on top of jgy-api.js (createApiClient) so that host allow-listing,
 * timeout, and error handling stay consistent with the rest of the Skill.
 *
 * Auth modes:
 *   - Bearer      : Authorization: Bearer <token>      — bind, me, detail
 *   - ClaimToken  : Authorization: ClaimToken <token>   — anonymous prize, detail
 *   - body token  : claim_token in request body          — reveal
 */

const { createApiClient } = require('./jgy-api');

function createLotteryApi({ bearer = null } = {}) {
  const client = createApiClient();
  const { businessApi, request } = client;

  // ── internal helpers ────────────────────────────────────────

  function bearerHeaders(bearerOverride) {
    const b = bearerOverride ?? bearer;
    const headers = {};
    if (b) headers.authorization = `Bearer ${b}`;
    return headers;
  }

  function claimTokenHeaders(claimToken) {
    return { authorization: `ClaimToken ${claimToken}` };
  }

  async function apiCall({ method = 'GET', path, body, headers = {} }) {
    const url = `${businessApi}${path}`;
    try {
      const data = await request(url, {
        method,
        headers,
        json: body ?? null,
      });
      return data;
    } catch (err) {
      if (err && err.code === 'HTTP_ERROR' && err.body && typeof err.body === 'object') {
        return err.body;
      }
      return {
        ok: false,
        code: err && err.code ? err.code : 'NETWORK_ERROR',
        message: '请求失败，请稍后重试。',
      };
    }
  }

  // ── public API ──────────────────────────────────────────────

  /**
   * POST /api/v1/lottery/reveal
   * Reveal a physical card.
   * Auth: optional Bearer (body always carries claim_token).
   * @param {object} params — { slug, claimToken }
   */
  function revealLottery({ slug, claimToken } = {}) {
    return apiCall({
      method: 'POST',
      path: '/lottery/reveal',
      body: { slug, claim_token: claimToken },
      headers: bearerHeaders(),
    });
  }

  /**
   * GET /api/v1/prizes/anonymous
   * Query prize info using anonymous claim token.
   * Auth: ClaimToken header.
   * @param {string} claimToken
   */
  function getAnonymousPrize(claimToken) {
    return apiCall({
      method: 'GET',
      path: '/prizes/anonymous',
      headers: claimTokenHeaders(claimToken),
    });
  }

  /**
   * GET /api/v1/prizes/:claim_id
   * Query a single prize detail.
   * Auth: ClaimToken or Bearer (caller decides via authMode).
   * @param {string} claimId
   * @param {object} [opts] — { claimToken? }  若提供则用 ClaimToken，否则用 Bearer
   */
  function getPrizeDetail(claimId, { claimToken } = {}) {
    const headers = claimToken
      ? claimTokenHeaders(claimToken)
      : bearerHeaders();
    return apiCall({
      method: 'GET',
      path: `/prizes/${encodeURIComponent(claimId)}`,
      headers,
    });
  }

  /**
   * POST /api/v1/prizes/bind
   * Bind an anonymous claim to the logged-in user's sub_id.
   * Auth: Bearer.  Body: { claim_token }.
   * @param {string} claimToken
   */
  function bindPrize(claimToken) {
    return apiCall({
      method: 'POST',
      path: '/prizes/bind',
      body: { claim_token: claimToken },
      headers: bearerHeaders(),
    });
  }

  /**
   * GET /api/v1/prizes/me
   * List all prizes for the currently logged-in user.
   * Auth: Bearer.
   */
  function getMyPrizes() {
    return apiCall({
      method: 'GET',
      path: '/prizes/me',
      headers: bearerHeaders(),
    });
  }

  return { revealLottery, getAnonymousPrize, getPrizeDetail, bindPrize, getMyPrizes };
}

module.exports = { createLotteryApi };
