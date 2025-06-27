#!/usr/bin/env python3
"""
Basic Accessibility Checker
A simple tool to perform basic accessibility checks on web content
"""

import re
import sys
from typing import List, Dict, Any


class AccessibilityChecker:
    """Basic accessibility checker for web content"""
    
    def __init__(self):
        self.issues = []
        
    def check_html_content(self, html_content: str) -> List[Dict[str, Any]]:
        """
        Perform basic accessibility checks on HTML content
        
        Args:
            html_content: HTML string to analyze
            
        Returns:
            List of accessibility issues found
        """
        self.issues = []
        
        # Check for images without alt text
        self._check_images_alt_text(html_content)
        
        # Check for proper heading structure
        self._check_heading_structure(html_content)
        
        # Check for form labels
        self._check_form_labels(html_content)
        
        # Check for empty links
        self._check_empty_links(html_content)
        
        return self.issues
    
    def _check_images_alt_text(self, html_content: str):
        """Check for images without alt text"""
        img_pattern = r'<img(?![^>]*alt\s*=)[^>]*>'
        missing_alt = re.findall(img_pattern, html_content, re.IGNORECASE)
        
        for img in missing_alt:
            self.issues.append({
                'type': 'missing_alt_text',
                'severity': 'high',
                'wcag': '1.1.1',
                'message': 'Image missing alt text',
                'element': img.strip(),
                'description': 'All images must have alternative text for screen readers'
            })
    
    def _check_heading_structure(self, html_content: str):
        """Check for proper heading structure (h1-h6)"""
        heading_pattern = r'<h([1-6])[^>]*>'
        headings = re.findall(heading_pattern, html_content, re.IGNORECASE)
        
        if headings:
            heading_levels = [int(h) for h in headings]
            
            # Check if first heading is h1
            if heading_levels[0] != 1:
                self.issues.append({
                    'type': 'heading_structure',
                    'severity': 'medium',
                    'wcag': '1.3.1',
                    'message': 'Page should start with h1 heading',
                    'description': 'Proper heading hierarchy helps screen reader navigation'
                })
            
            # Check for skipped heading levels
            for i in range(1, len(heading_levels)):
                if heading_levels[i] > heading_levels[i-1] + 1:
                    self.issues.append({
                        'type': 'heading_structure',
                        'severity': 'medium',
                        'wcag': '1.3.1',
                        'message': f'Heading level skipped from h{heading_levels[i-1]} to h{heading_levels[i]}',
                        'description': 'Heading levels should not skip (e.g., h2 should not directly follow h4)'
                    })
    
    def _check_form_labels(self, html_content: str):
        """Check for form inputs without labels"""
        input_pattern = r'<input(?![^>]*(?:type\s*=\s*["\'](?:hidden|submit|button)["\']|aria-label\s*=|title\s*=))[^>]*>'
        inputs_without_labels = re.findall(input_pattern, html_content, re.IGNORECASE)
        
        for input_elem in inputs_without_labels:
            # Check if there's a corresponding label
            input_id_match = re.search(r'id\s*=\s*["\']([^"\']*)["\']', input_elem)
            if input_id_match:
                input_id = input_id_match.group(1)
                label_pattern = f'<label[^>]*for\\s*=\\s*["\\\']?{input_id}["\\\']?'
                if not re.search(label_pattern, html_content, re.IGNORECASE):
                    self.issues.append({
                        'type': 'missing_form_label',
                        'severity': 'high',
                        'wcag': '1.3.1',
                        'message': 'Form input missing label',
                        'element': input_elem.strip(),
                        'description': 'All form inputs need labels for screen reader users'
                    })
    
    def _check_empty_links(self, html_content: str):
        """Check for links without text content"""
        link_pattern = r'<a[^>]*>(\s*)</a>'
        empty_links = re.findall(link_pattern, html_content, re.IGNORECASE)
        
        if empty_links:
            self.issues.append({
                'type': 'empty_link',
                'severity': 'high',
                'wcag': '2.4.4',
                'message': 'Empty link found',
                'description': 'Links must have descriptive text or aria-label for screen readers'
            })
    
    def generate_report(self) -> str:
        """Generate a formatted accessibility report"""
        if not self.issues:
            return "✅ No accessibility issues found!"
        
        report = "🔍 Accessibility Issues Found\n"
        report += "=" * 40 + "\n\n"
        
        # Group by severity
        critical = [i for i in self.issues if i['severity'] == 'critical']
        high = [i for i in self.issues if i['severity'] == 'high']
        medium = [i for i in self.issues if i['severity'] == 'medium']
        low = [i for i in self.issues if i['severity'] == 'low']
        
        for severity, issues in [('CRITICAL', critical), ('HIGH', high), ('MEDIUM', medium), ('LOW', low)]:
            if issues:
                report += f"\n🚨 {severity} SEVERITY ({len(issues)} issues)\n"
                report += "-" * 30 + "\n"
                
                for issue in issues:
                    report += f"• WCAG {issue['wcag']}: {issue['message']}\n"
                    report += f"  {issue['description']}\n"
                    if 'element' in issue:
                        report += f"  Element: {issue['element']}\n"
                    report += "\n"
        
        return report


def main():
    """Command line interface for the accessibility checker"""
    if len(sys.argv) != 2:
        print("Usage: python accessibility_checker.py <html_file>")
        sys.exit(1)
    
    html_file = sys.argv[1]
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{html_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    checker = AccessibilityChecker()
    issues = checker.check_html_content(html_content)
    
    print(checker.generate_report())
    
    # Exit with error code if issues found
    if issues:
        sys.exit(1)


if __name__ == "__main__":
    main()