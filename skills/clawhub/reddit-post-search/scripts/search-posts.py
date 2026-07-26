import argparse
import json
import sys


def main():
    sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    parser = argparse.ArgumentParser(description='Generate JS to fetch one page of Reddit posts')
    parser.add_argument('--query', default='', help='Search query string')
    parser.add_argument('--subreddit', default='', help='Subreddit name without r/ prefix')
    parser.add_argument('--sort', default='relevance',
                        help='Sort order: relevance|hot|top|new|comments')
    parser.add_argument('--timeframe', default='all',
                        help='Time window: all|year|month|week|day|hour')
    parser.add_argument('--limit', type=int, default=100,
                        help='Posts per page (1-100)')
    parser.add_argument('--after', default='',
                        help='Pagination cursor from previous response after field')
    parser.add_argument('--include-nsfw', dest='include_nsfw', default='false',
                        help='Include NSFW posts: true|false')
    parser.add_argument('--date-from', dest='date_from', default='',
                        help='Lower date bound ISO-8601 or YYYY-MM-DD')
    parser.add_argument('--date-to', dest='date_to', default='',
                        help='Upper date bound ISO-8601 or YYYY-MM-DD')
    parser.add_argument('--strict-token-filter', dest='strict_token_filter', default='false',
                        help='Filter posts missing any query token: true|false')
    parser.add_argument('--url', default='',
                        help='Direct Reddit URL (overrides query/subreddit params)')
    parser.add_argument('--query-label', dest='query_label', default='',
                        help='Label for the query field in output records')
    args = parser.parse_args()

    query_label = args.query_label or args.query or args.subreddit or args.url

    js = f"""
(async () => {{
  try {{
    const query          = {json.dumps(args.query)};
    const subreddit      = {json.dumps(args.subreddit)};
    const sort           = {json.dumps(args.sort)};
    const timeframe      = {json.dumps(args.timeframe)};
    const limit          = Math.min({args.limit}, 100);
    const after          = {json.dumps(args.after)};
    const includeNsfw    = {json.dumps(args.include_nsfw)} === 'true';
    const dateFrom       = {json.dumps(args.date_from)};
    const dateTo         = {json.dumps(args.date_to)};
    const strictFilter   = {json.dumps(args.strict_token_filter)} === 'true';
    const directUrl      = {json.dumps(args.url)};
    const queryLabel     = {json.dumps(query_label)};

    // Build Reddit JSON API endpoint
    const afterParam = after ? '&after=' + after : '';
    const nsfwParam  = includeNsfw ? '&include_over_18=on' : '';
    let endpoint;

    if (directUrl) {{
      let u = directUrl.replace(/\\/+$/, '');
      if (u.includes('/search?')) {{
        endpoint = u.replace('/search?', '/search.json?') + '&limit=' + limit + afterParam;
      }} else if (/\\/comments\\/([a-z0-9]+)/.test(u)) {{
        const m = u.match(/\\/comments\\/([a-z0-9]+)/);
        endpoint = 'https://www.reddit.com/comments/' + m[1] + '.json?limit=' + limit + afterParam;
      }} else if (/\\/r\\/[^\\/]+$/.test(u)) {{
        endpoint = u + '.json?sort=' + sort + '&t=' + timeframe + '&limit=' + limit + afterParam;
      }} else if (/\\/user\\/[^\\/]+$/.test(u)) {{
        endpoint = u + '/submitted.json?sort=' + sort + '&t=' + timeframe + '&limit=' + limit + afterParam;
      }} else {{
        endpoint = u + '.json?limit=' + limit + afterParam;
      }}
    }} else if (subreddit && query) {{
      endpoint = 'https://www.reddit.com/r/' + subreddit +
        '/search.json?q=' + encodeURIComponent(query) +
        '&restrict_sr=1&sort=' + sort + '&t=' + timeframe +
        '&limit=' + limit + afterParam + nsfwParam;
    }} else if (subreddit) {{
      endpoint = 'https://www.reddit.com/r/' + subreddit +
        '.json?sort=' + sort + '&t=' + timeframe +
        '&limit=' + limit + afterParam;
    }} else {{
      endpoint = 'https://www.reddit.com/search.json?q=' + encodeURIComponent(query) +
        '&sort=' + sort + '&t=' + timeframe +
        '&limit=' + limit + afterParam + nsfwParam;
    }}

    const resp = await fetch(endpoint, {{ headers: {{ 'Accept': 'application/json' }} }});
    if (!resp.ok) {{
      return JSON.stringify({{ error: true, message: 'HTTP ' + resp.status + ' from ' + endpoint }});
    }}
    const data = await resp.json();
    if (!data.data) {{
      return JSON.stringify({{ error: true, message: 'Unexpected response shape', endpoint }});
    }}

    const now = new Date().toISOString();

    // Transform posts
    let posts = (data.data.children || []).filter(c => c.kind === 't3').map(c => {{
      const p = c.data;
      const ageHours = Math.round((Date.now() / 1000 - p.created_utc) / 3600 * 10) / 10;
      const isDeleted = p.selftext === '[deleted]' || p.selftext === '[removed]' || p.author === '[deleted]';
      const outboundHost = (() => {{ try {{ return p.url_overridden_by_dest ? new URL(p.url_overridden_by_dest).hostname : null; }} catch(e) {{ return null; }} }})();
      return {{
        kind: 'post',
        query: queryLabel,
        id: p.id,
        title: p.title,
        body: p.selftext || null,
        author: p.author,
        score: p.score,
        upvote_ratio: p.upvote_ratio != null ? p.upvote_ratio : null,
        num_comments: p.num_comments,
        subreddit: p.subreddit,
        created_utc: new Date(p.created_utc * 1000).toISOString(),
        url: 'https://www.reddit.com' + p.permalink,
        permalink: p.permalink,
        canonical_url: 'https://www.reddit.com' + p.permalink,
        old_reddit_url: 'https://old.reddit.com' + p.permalink,
        flair: p.link_flair_text || null,
        post_hint: p.post_hint || null,
        over_18: p.over_18,
        is_self: p.is_self,
        spoiler: p.spoiler,
        locked: p.locked,
        is_video: p.is_video,
        is_gallery: p.is_gallery || false,
        hidden: p.hidden || false,
        edited: p.edited || false,
        archived: p.archived,
        pinned: p.pinned,
        domain: p.domain || null,
        thumbnail: p.thumbnail || null,
        url_overridden_by_dest: p.url_overridden_by_dest || null,
        num_duplicates: p.num_duplicates || 0,
        subreddit_id: p.subreddit_id || null,
        subreddit_name_prefixed: p.subreddit_name_prefixed || null,
        subreddit_subscribers: p.subreddit_subscribers || null,
        media: p.media || null,
        age_hours: ageHours,
        retrieved_at: now,
        has_media: !!(p.is_video || p.is_gallery || (p.post_hint && ['image', 'rich:video'].includes(p.post_hint))),
        gallery_count: p.gallery_data?.items?.length || 0,
        outbound_url_host: outboundHost,
        title_length: (p.title || '').length,
        body_length: (p.selftext || '').length,
        word_count: ((p.title || '') + ' ' + (p.selftext || '')).split(/\\s+/).filter(Boolean).length,
        score_per_hour: ageHours > 0.01 ? Math.round(p.score / Math.max(ageHours, 0.01) * 100) / 100 : 0,
        comments_per_hour: ageHours > 0.01 ? Math.round(p.num_comments / Math.max(ageHours, 0.01) * 100) / 100 : 0,
        is_deleted_or_removed: isDeleted,
        engagement_total: (p.score || 0) + (p.num_comments || 0),
        comment_to_score_ratio: p.score > 0 ? Math.round(p.num_comments / p.score * 10000) / 10000 : null,
        is_high_engagement: (p.score || 0) > 1000 || (p.num_comments || 0) > 100,
        stickied: p.stickied,
        distinguished: p.distinguished || null,
        score_hidden: p.hide_score || false,
        total_awards_received: p.total_awards_received || 0,
        gilded: p.gilded || 0,
        num_crossposts: p.num_crossposts || 0,
        is_original_content: p.is_original_content || false,
        author_fullname: p.author_fullname || null,
        author_flair_text: p.author_flair_text || null,
        author_premium: p.author_premium || false,
        crosspost_parent_list: p.crosspost_parent_list || null
      }};
    }});

    // Date filtering (record-level, applied after fetch)
    if (dateFrom) {{
      const fromTs = new Date(dateFrom).getTime();
      posts = posts.filter(p => new Date(p.created_utc).getTime() >= fromTs);
    }}
    if (dateTo) {{
      const toTs = new Date(dateTo).getTime();
      posts = posts.filter(p => new Date(p.created_utc).getTime() <= toTs);
    }}

    // Strict token filter: every query token must appear in title+body+url
    if (strictFilter && query) {{
      const tokens = query.toLowerCase().replace(/"/g, '').split(/\\s+/).filter(Boolean);
      posts = posts.filter(p => {{
        const text = ((p.title || '') + ' ' + (p.body || '') + ' ' + (p.url || '')).toLowerCase();
        return tokens.every(t => text.includes(t));
      }});
    }}

    return JSON.stringify({{
      posts: posts,
      after: data.data.after || null,
      count: posts.length,
      has_more: !!data.data.after
    }});
  }} catch (e) {{
    return JSON.stringify({{ error: true, message: e.message }});
  }}
}})()
"""
    print(js)


if __name__ == '__main__':
    main()
