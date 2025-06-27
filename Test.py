#!/usr/bin/env python3
"""
Test suite for accessibility checker functionality
"""

import unittest
import sys
import os

# Add the current directory to Python path to import accessibility_checker
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from accessibility_checker import AccessibilityChecker


class TestAccessibilityChecker(unittest.TestCase):
    """Test cases for AccessibilityChecker class"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.checker = AccessibilityChecker()
    
    def test_missing_alt_text(self):
        """Test detection of images without alt text"""
        html = '<img src="test.jpg">'
        issues = self.checker.check_html_content(html)
        
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0]['type'], 'missing_alt_text')
        self.assertEqual(issues[0]['wcag'], '1.1.1')
    
    def test_image_with_alt_text(self):
        """Test that images with alt text don't trigger issues"""
        html = '<img src="test.jpg" alt="Test image">'
        issues = self.checker.check_html_content(html)
        
        # Should not find any issues
        alt_issues = [i for i in issues if i['type'] == 'missing_alt_text']
        self.assertEqual(len(alt_issues), 0)
    
    def test_heading_structure_valid(self):
        """Test valid heading structure"""
        html = '<h1>Title</h1><h2>Section</h2><h3>Subsection</h3>'
        issues = self.checker.check_html_content(html)
        
        # Should not find heading structure issues
        heading_issues = [i for i in issues if i['type'] == 'heading_structure']
        self.assertEqual(len(heading_issues), 0)
    
    def test_heading_structure_skipped_level(self):
        """Test detection of skipped heading levels"""
        html = '<h1>Title</h1><h3>Section</h3>'
        issues = self.checker.check_html_content(html)
        
        heading_issues = [i for i in issues if i['type'] == 'heading_structure']
        self.assertEqual(len(heading_issues), 1)
        self.assertIn('skipped', heading_issues[0]['message'])
    
    def test_form_with_proper_labels(self):
        """Test form with proper labels"""
        html = '''
        <label for="username">Username:</label>
        <input type="text" id="username" name="username">
        '''
        issues = self.checker.check_html_content(html)
        
        label_issues = [i for i in issues if i['type'] == 'missing_form_label']
        self.assertEqual(len(label_issues), 0)
    
    def test_form_without_labels(self):
        """Test detection of form inputs without labels"""
        html = '<input type="text" id="username" name="username">'
        issues = self.checker.check_html_content(html)
        
        label_issues = [i for i in issues if i['type'] == 'missing_form_label']
        self.assertEqual(len(label_issues), 1)
        self.assertEqual(label_issues[0]['wcag'], '1.3.1')
    
    def test_empty_links(self):
        """Test detection of empty links"""
        html = '<a href="#"></a>'
        issues = self.checker.check_html_content(html)
        
        link_issues = [i for i in issues if i['type'] == 'empty_link']
        self.assertEqual(len(link_issues), 1)
        self.assertEqual(link_issues[0]['wcag'], '2.4.4')
    
    def test_links_with_content(self):
        """Test that links with content don't trigger issues"""
        html = '<a href="#">Link text</a>'
        issues = self.checker.check_html_content(html)
        
        link_issues = [i for i in issues if i['type'] == 'empty_link']
        self.assertEqual(len(link_issues), 0)
    
    def test_report_generation_no_issues(self):
        """Test report generation when no issues found"""
        html = '<h1>Good HTML</h1><img src="test.jpg" alt="Good image">'
        self.checker.check_html_content(html)
        
        report = self.checker.generate_report()
        self.assertIn("No accessibility issues found", report)
    
    def test_report_generation_with_issues(self):
        """Test report generation when issues are found"""
        html = '<img src="test.jpg">'  # Missing alt text
        self.checker.check_html_content(html)
        
        report = self.checker.generate_report()
        self.assertIn("Accessibility Issues Found", report)
        self.assertIn("HIGH SEVERITY", report)
        self.assertIn("WCAG 1.1.1", report)


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)