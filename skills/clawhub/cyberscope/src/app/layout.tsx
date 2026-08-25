import type { Metadata } from "next";
import type { ReactNode } from "react";
import "./globals.css";

export const metadata: Metadata = {
  title: "CyberScope — Cyber Operations Search Engine",
  description:
    "Specialized search engine for Internet Data Leak Prevention, Surveillance, Censorship & Cyber Operations Methods. Browse 62 documented techniques across 10 categories with curated resources.",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" className="dark">
      <body className="min-h-screen bg-gray-950 text-gray-100 antialiased">
        {children}
      </body>
    </html>
  );
}
