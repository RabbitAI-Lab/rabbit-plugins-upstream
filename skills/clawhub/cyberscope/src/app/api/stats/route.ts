import { NextRequest, NextResponse } from "next/server";
import { db } from "@/db";
import { categories, methods, resources, searchHistory } from "@/db/schema";
import { sql, desc } from "drizzle-orm";
import {
  enforceSecurityMiddleware,
  wrapSecureResponse,
  secureErrorResponse,
  SECURITY_CONFIG,
} from "@/lib/security";

export const dynamic = "force-dynamic";

export async function GET(request: NextRequest) {
  // 1. Security enforcement
  const securityResult = await enforceSecurityMiddleware(request, "stats");
  if (!securityResult.allowed) {
    return securityResult.response;
  }
  const { context } = securityResult;

  try {
    // 2. Execute count queries with parameterized statements
    const [catCount] = await db
      .select({ count: sql<number>`count(*)::int` })
      .from(categories);
    const [methCount] = await db
      .select({ count: sql<number>`count(*)::int` })
      .from(methods);
    const [resCount] = await db
      .select({ count: sql<number>`count(*)::int` })
      .from(resources);
    const [searchCount] = await db
      .select({ count: sql<number>`count(*)::int` })
      .from(searchHistory);

    // 3. Get recent searches (limited and without PII)
    const recentSearches = await db
      .select({
        id: searchHistory.id,
        query: searchHistory.query,
        resultsCount: searchHistory.resultsCount,
        categoryFilter: searchHistory.categoryFilter,
        createdAt: searchHistory.createdAt,
      })
      .from(searchHistory)
      .orderBy(desc(searchHistory.createdAt))
      .limit(10);

    // 4. Get top searches
    const topSearches = await db
      .select({
        query: searchHistory.query,
        count: sql<number>`count(*)::int`,
      })
      .from(searchHistory)
      .groupBy(searchHistory.query)
      .orderBy(desc(sql`count(*)`))
      .limit(10);

    // 5. Return secure response
    const response = NextResponse.json({
      stats: {
        categories: catCount.count,
        methods: methCount.count,
        resources: resCount.count,
        totalSearches: searchCount.count,
      },
      recentSearches,
      topSearches,
    });

    return wrapSecureResponse(response, context, "stats");
  } catch (error) {
    // Log error internally but don't expose details
    console.error("[STATS ERROR]", error);
    return wrapSecureResponse(
      secureErrorResponse(SECURITY_CONFIG.errors.generic, 500),
      context,
      "stats"
    );
  }
}
