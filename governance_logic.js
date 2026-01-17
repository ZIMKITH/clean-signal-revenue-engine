/**
 * THE GLASS BOX REVENUE ENGINE
 * Component: Normalization & Governance Logic
 */

// 1. INGESTION
const root = $input.item.json;
const data = root.body || root; 

// Fail-safe extraction
const rawName = data.company_name || data.company || ""; 
const newsSummary = (data.news_summary || "").toLowerCase();

// 2. NORMALIZATION (The "Laundromat")
const cleanName = rawName
  .replace(/(\s|,|\.)+(Inc|LLC|Ltd|Limited|Corp|Corporation|GmbH|Co)\.?$/i, "")
  .trim();

// 3. GOVERNANCE (The "Watchdog")
const negativeKeywords = ["bankrupt", "fraud", "lawsuit", "investigation", "layoff", "scandal"];
let status = "PASS";
let reason = "None";

for (const word of negativeKeywords) {
  if (newsSummary.includes(word)) {
    status = "FAIL";
    reason = `Risk detected: ${word}`;
    break; 
  }
}

// 4. OUTPUT
return {
  ...data, 
  normalized_company_name: cleanName,
  safety_status: status,
  flag_reason: reason,
  processed_at: new Date().toISOString()
};
