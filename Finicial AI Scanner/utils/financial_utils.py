"""
Financial utilities for processing and formatting financial data.
"""
import re
from typing import Dict, List, Union

def extract_financial_metrics(text: str) -> Dict[str, Union[float, str]]:
    """
    Extract financial metrics from analyzed text.
    
    Args:
        text (str): Analyzed text containing financial information
        
    Returns:
        Dict[str, Union[float, str]]: Dictionary of extracted metrics
    """
    metrics = {}
    
    # Common financial metric patterns
    patterns = {
        'currency': r'(?:EUR|USD|GBP|JPY)\s*(\d+(?:\.\d+)?(?:\s*[bBmM]illion)?)',
        'percentage': r'(\d+(?:\.\d+)?)\s*%',
        'ratio': r'(\d+(?:\.\d+)?)\s*:\s*(\d+(?:\.\d+)?)'
    }
    
    # Extract currencies
    currency_matches = re.finditer(patterns['currency'], text)
    for match in currency_matches:
        context = text[max(0, match.start() - 50):match.end() + 50]
        key = _get_metric_key(context)
        if key:
            metrics[key] = match.group(0)
    
    # Extract percentages
    percentage_matches = re.finditer(patterns['percentage'], text)
    for match in percentage_matches:
        context = text[max(0, match.start() - 50):match.end() + 50]
        key = _get_metric_key(context)
        if key:
            metrics[key] = f"{match.group(1)}%"
    
    return metrics

def _get_metric_key(context: str) -> str:
    """
    Get appropriate key for a metric based on its context.
    
    Args:
        context (str): Text surrounding the metric
        
    Returns:
        str: Appropriate key for the metric
    """
    common_metrics = {
        'net profit': 'Net Profit',
        'revenue': 'Revenue',
        'eps': 'Earnings Per Share',
        'roe': 'Return on Equity',
        'cost/income': 'Cost/Income Ratio',
        'tier 1': 'Tier 1 Ratio'
    }
    
    for keyword, metric_name in common_metrics.items():
        if keyword.lower() in context.lower():
            return metric_name
    
    return None

def format_financial_summary(metrics: Dict[str, Union[float, str]]) -> str:
    """
    Format financial metrics into a readable summary.
    
    Args:
        metrics (Dict[str, Union[float, str]]): Dictionary of financial metrics
        
    Returns:
        str: Formatted summary text
    """
    if not metrics:
        return "No financial metrics found."
    
    summary = "Financial Summary:\n\n"
    
    # Group metrics by category
    categories = {
        'Profitability': ['Net Profit', 'Revenue', 'Earnings Per Share'],
        'Efficiency': ['Cost/Income Ratio', 'Return on Equity'],
        'Capital': ['Tier 1 Ratio']
    }
    
    for category, metric_keys in categories.items():
        category_metrics = {k: v for k, v in metrics.items() if k in metric_keys}
        if category_metrics:
            summary += f"{category}:\n"
            for key, value in category_metrics.items():
                summary += f"• {key}: {value}\n"
            summary += "\n"
    
    return summary 