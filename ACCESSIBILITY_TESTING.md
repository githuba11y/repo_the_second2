# Accessibility Testing Guidelines

## Overview

This document provides comprehensive guidelines for conducting accessibility audits using this repository's tools and templates.

## Testing Methodology

### 1. Automated Testing
Use automated tools as a starting point, but remember they only catch 20-30% of accessibility issues.

**Tools to use:**
- `accessibility_checker.py` (included in this repo)
- axe-core browser extension
- WAVE Web Accessibility Evaluator
- Lighthouse accessibility audit

### 2. Manual Testing

#### Keyboard Navigation Testing
1. **Tab through all interactive elements**
   - Ensure logical tab order
   - Verify all interactive elements are reachable
   - Check that focus indicators are visible
   - Test skip links functionality

2. **Test with keyboard only**
   - Navigate using Tab, Shift+Tab, Enter, Space, Arrow keys
   - Ensure all functionality is available without mouse
   - Test dropdown menus, modal dialogs, carousels

#### Screen Reader Testing
1. **Test with at least one screen reader:**
   - **Windows:** NVDA (free) or JAWS
   - **macOS:** VoiceOver (built-in)
   - **Mobile:** TalkBack (Android) or VoiceOver (iOS)

2. **Key testing points:**
   - Page structure navigation (headings, landmarks)
   - Form accessibility (labels, error messages)
   - Image alternative text
   - Link context and purpose
   - Data table accessibility

### 3. Visual Testing

#### Color and Contrast
- Test color contrast ratios (4.5:1 for normal text, 3:1 for large text)
- Ensure information isn't conveyed by color alone
- Test with different color vision simulations

#### Focus Management
- Verify focus indicators are visible and consistent
- Check focus trap in modals and dropdown menus
- Test focus restoration after modal close

## Testing Checklist

### Page Structure
- [ ] Page has proper heading hierarchy (h1-h6)
- [ ] Landmarks are used appropriately (header, nav, main, aside, footer)
- [ ] Page has descriptive title
- [ ] Language is specified in HTML lang attribute

### Images and Media
- [ ] All images have appropriate alt text
- [ ] Decorative images have empty alt attributes (alt="")
- [ ] Complex images have detailed descriptions
- [ ] Videos have captions and transcripts

### Forms
- [ ] All form fields have labels
- [ ] Required fields are clearly indicated
- [ ] Error messages are descriptive and associated with fields
- [ ] Form has logical tab order
- [ ] Fieldsets and legends used for grouped form elements

### Links and Navigation
- [ ] Link text is descriptive (avoid "click here", "read more")
- [ ] Navigation is consistent across pages
- [ ] Breadcrumbs provided where appropriate
- [ ] Skip links available for keyboard users

### Interactive Elements
- [ ] All buttons have accessible names
- [ ] ARIA labels provided where needed
- [ ] State changes are announced to screen readers
- [ ] Custom controls follow ARIA authoring practices

## Common Issues and Solutions

### Issue: Images without alt text
**Solution:** Add appropriate alt attributes
```html
<!-- Good -->
<img src="chart.png" alt="Sales increased 25% from Q1 to Q2">

<!-- Bad -->
<img src="chart.png">
```

### Issue: Poor heading structure
**Solution:** Use logical heading hierarchy
```html
<!-- Good -->
<h1>Main Page Title</h1>
<h2>Section Title</h2>
<h3>Subsection Title</h3>

<!-- Bad -->
<h1>Main Page Title</h1>
<h3>Section Title</h3> <!-- Skipped h2 -->
```

### Issue: Form fields without labels
**Solution:** Properly associate labels with form controls
```html
<!-- Good -->
<label for="email">Email Address</label>
<input type="email" id="email" name="email">

<!-- Bad -->
<input type="email" name="email" placeholder="Email Address">
```

## Severity Guidelines

### Critical
- Prevents task completion for users with disabilities
- Complete loss of functionality
- Legal compliance issues

### High
- Significantly impacts user experience
- Major barriers to content access
- WCAG Level A violations

### Medium
- Some impact on user experience
- Minor barriers that affect usability
- WCAG Level AA violations

### Low
- Minimal impact but improves overall accessibility
- Enhancement opportunities
- WCAG Level AAA considerations

## Reporting Guidelines

When creating accessibility issue reports:

1. **Use the provided issue template**
2. **Be specific about the barrier**
3. **Include reproduction steps**
4. **Specify assistive technology used**
5. **Reference relevant WCAG criteria**
6. **Suggest potential solutions**
7. **Include screenshots or recordings when helpful**

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Screen Reader Testing Guide](https://webaim.org/articles/screenreader_testing/)
- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [Color Contrast Analyzers](https://www.tpgi.com/color-contrast-checker/)