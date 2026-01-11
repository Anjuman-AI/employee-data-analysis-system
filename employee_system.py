"""
Employee Data Analysis System
=============================

A comprehensive Python system for managing and analyzing employee data.

Author: [Your Name]
Date: January 2026
GitHub: [Your GitHub URL]
Purpose: Data Engineering Portfolio Project (Day 1 - Python Fundamentals)

Features:
- Employee data generation with realistic attributes
- Statistical analysis by department
- Performance tracking and ranking
- Salary distribution analysis
- CSV export functionality
- Professional reporting system

Technologies:
- Python 3.x
- Object-Oriented Programming (OOP)
- CSV file handling
- Data structures (Lists, Dictionaries)
- Statistical calculations
"""

import csv
import random
from datetime import datetime, timedelta
from typing import List, Dict


class Employee:
    """
    Represents an individual employee with their attributes.
    
    Attributes:
        emp_id (str): Unique employee identifier (e.g., 'EMP0001')
        name (str): Full name of employee
        department (str): Department name
        salary (float): Monthly salary in local currency
        joining_date (str): Date of joining (YYYY-MM-DD format)
        performance_score (float): Performance rating (1.0 to 10.0)
    """
    
    def __init__(self, emp_id: str, name: str, department: str, 
                 salary: float, joining_date: str, performance_score: float):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        self.joining_date = joining_date
        self.performance_score = performance_score
    
    def to_dict(self) -> Dict:
        """Convert employee object to dictionary for CSV export."""
        return {
            'emp_id': self.emp_id,
            'name': self.name,
            'department': self.department,
            'salary': self.salary,
            'joining_date': self.joining_date,
            'performance_score': self.performance_score
        }
    
    def __str__(self) -> str:
        """String representation of employee."""
        return f"Employee({self.emp_id}, {self.name}, {self.department})"
    
    def __repr__(self) -> str:
        """Detailed representation for debugging."""
        return f"Employee(id={self.emp_id}, name={self.name}, dept={self.department}, salary={self.salary})"


class EmployeeDataGenerator:
    """
    Generate realistic employee data for analysis and testing.
    
    This class provides methods to create employee records with
    realistic attributes including names, departments, salaries,
    and performance scores.
    """
    
    # Class constants for data generation
    DEPARTMENTS = ['Engineering', 'Sales', 'Marketing', 'HR', 'Finance']
    
    FIRST_NAMES = [
        'Ahmed', 'Fatima', 'Mohammad', 'Ayesha', 'Karim', 
        'Nadia', 'Rahim', 'Zara', 'Ali', 'Samira',
        'Hassan', 'Laila', 'Omar', 'Sara', 'Tariq',
        'Amina', 'Bilal', 'Huda', 'Ibrahim', 'Maryam'
    ]
    
    LAST_NAMES = [
        'Khan', 'Ahmed', 'Rahman', 'Hassan', 'Ali', 
        'Mahmud', 'Hossain', 'Islam', 'Chowdhury', 'Akter',
        'Siddiqui', 'Malik', 'Sheikh', 'Hussain', 'Begum'
    ]
    
    @staticmethod
    def generate_employees(num_employees: int = 100) -> List[Employee]:
        """
        Generate specified number of employee records.
        
        Args:
            num_employees (int): Number of employees to generate (default: 100)
            
        Returns:
            List[Employee]: List of Employee objects with generated data
            
        Example:
            >>> generator = EmployeeDataGenerator()
            >>> employees = generator.generate_employees(50)
            >>> len(employees)
            50
        """
        employees = []
        
        # Base salaries by department (realistic ranges)
        base_salaries = {
            'Engineering': 80000,
            'Sales': 60000,
            'Marketing': 55000,
            'HR': 50000,
            'Finance': 70000
        }
        
        for i in range(1, num_employees + 1):
            # Generate employee ID (e.g., EMP0001, EMP0002, ...)
            emp_id = f"EMP{i:04d}"
            
            # Generate full name
            first_name = random.choice(EmployeeDataGenerator.FIRST_NAMES)
            last_name = random.choice(EmployeeDataGenerator.LAST_NAMES)
            name = f"{first_name} {last_name}"
            
            # Assign department
            department = random.choice(EmployeeDataGenerator.DEPARTMENTS)
            
            # Generate salary (base + random variation)
            base = base_salaries[department]
            variation = random.randint(-10000, 30000)
            salary = max(base + variation, 30000)  # Minimum salary: 30000
            
            # Generate joining date (within last 5 years)
            days_ago = random.randint(0, 1825)  # 5 years = ~1825 days
            joining_date = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d')
            
            # Generate performance score (5.0 to 10.0)
            performance_score = round(random.uniform(5.0, 10.0), 1)
            
            # Create employee object
            employee = Employee(
                emp_id=emp_id,
                name=name,
                department=department,
                salary=salary,
                joining_date=joining_date,
                performance_score=performance_score
            )
            
            employees.append(employee)
        
        return employees


class EmployeeAnalyzer:
    """
    Analyze employee data and generate insights.
    
    This class provides methods to perform statistical analysis
    on employee data including department-wise statistics,
    performance rankings, and salary distributions.
    """
    
    def __init__(self, employees: List[Employee]):
        """
        Initialize analyzer with employee data.
        
        Args:
            employees (List[Employee]): List of Employee objects to analyze
        """
        self.employees = employees
    
    def get_department_statistics(self) -> Dict:
        """
        Calculate comprehensive statistics by department.
        
        Returns:
            Dict: Department-wise statistics including:
                - count: Number of employees
                - total_salary: Sum of all salaries
                - avg_salary: Average salary
                - total_performance: Sum of performance scores
                - avg_performance: Average performance score
        """
        dept_data = {}
        
        # Aggregate data by department
        for emp in self.employees:
            dept = emp.department
            
            if dept not in dept_data:
                dept_data[dept] = {
                    'count': 0,
                    'total_salary': 0,
                    'total_performance': 0,
                    'employees': []
                }
            
            dept_data[dept]['count'] += 1
            dept_data[dept]['total_salary'] += emp.salary
            dept_data[dept]['total_performance'] += emp.performance_score
            dept_data[dept]['employees'].append(emp)
        
        # Calculate averages
        for dept in dept_data:
            count = dept_data[dept]['count']
            dept_data[dept]['avg_salary'] = dept_data[dept]['total_salary'] / count
            dept_data[dept]['avg_performance'] = dept_data[dept]['total_performance'] / count
        
        return dept_data
    
    def get_top_performers(self, n: int = 10) -> List[Employee]:
        """
        Get top N performing employees.
        
        Args:
            n (int): Number of top performers to return (default: 10)
            
        Returns:
            List[Employee]: Top N employees sorted by performance score
        """
        sorted_employees = sorted(
            self.employees, 
            key=lambda e: e.performance_score, 
            reverse=True
        )
        return sorted_employees[:n]
    
    def get_salary_range_distribution(self) -> Dict:
        """
        Get distribution of employees across salary ranges.
        
        Returns:
            Dict: Count of employees in each salary range
        """
        ranges = {
            '0-50k': 0,
            '50k-70k': 0,
            '70k-90k': 0,
            '90k-100k': 0,
            '100k+': 0
        }
        
        for emp in self.employees:
            if emp.salary < 50000:
                ranges['0-50k'] += 1
            elif emp.salary < 70000:
                ranges['50k-70k'] += 1
            elif emp.salary < 90000:
                ranges['70k-90k'] += 1
            elif emp.salary < 100000:
                ranges['90k-100k'] += 1
            else:
                ranges['100k+'] += 1
        
        return ranges
    
    def generate_report(self) -> str:
        """
        Generate comprehensive analysis report.
        
        Returns:
            str: Formatted report text with all analysis results
        """
        lines = []
        
        # Header
        lines.append("=" * 80)
        lines.append("EMPLOYEE DATA ANALYSIS REPORT")
        lines.append("=" * 80)
        lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"Total Employees Analyzed: {len(self.employees)}")
        lines.append("")
        
        # Department Statistics
        lines.append("DEPARTMENT STATISTICS:")
        lines.append("-" * 80)
        dept_stats = self.get_department_statistics()
        
        for dept, stats in sorted(dept_stats.items()):
            lines.append(f"\n{dept}:")
            lines.append(f"  Number of Employees: {stats['count']}")
            lines.append(f"  Average Salary: ${stats['avg_salary']:,.2f}")
            lines.append(f"  Average Performance Score: {stats['avg_performance']:.2f}/10")
        
        lines.append("")
        
        # Top Performers
        lines.append("TOP 10 PERFORMERS:")
        lines.append("-" * 80)
        top_performers = self.get_top_performers(10)
        
        for rank, emp in enumerate(top_performers, 1):
            lines.append(
                f"{rank:2d}. {emp.name:25s} ({emp.department:12s}) - "
                f"Score: {emp.performance_score}/10"
            )
        
        lines.append("")
        
        # Salary Distribution
        lines.append("SALARY DISTRIBUTION:")
        lines.append("-" * 80)
        salary_dist = self.get_salary_range_distribution()
        
        for range_name, count in salary_dist.items():
            percentage = (count / len(self.employees)) * 100
            bar = "█" * int(percentage / 2)  # Visual bar
            lines.append(f"{range_name:12s}: {count:3d} employees ({percentage:5.1f}%) {bar}")
        
        lines.append("")
        
        # Summary Statistics
        lines.append("OVERALL STATISTICS:")
        lines.append("-" * 80)
        
        all_salaries = [emp.salary for emp in self.employees]
        all_performances = [emp.performance_score for emp in self.employees]
        
        lines.append(f"Average Salary (All Departments): ${sum(all_salaries) / len(all_salaries):,.2f}")
        lines.append(f"Median Salary: ${sorted(all_salaries)[len(all_salaries) // 2]:,.2f}")
        lines.append(f"Salary Range: ${min(all_salaries):,.2f} - ${max(all_salaries):,.2f}")
        lines.append(f"Average Performance Score: {sum(all_performances) / len(all_performances):.2f}/10")
        
        lines.append("")
        lines.append("=" * 80)
        lines.append("End of Report")
        lines.append("=" * 80)
        
        return "\n".join(lines)


class FileManager:
    """
    Handle file operations for employee data.
    
    Provides methods to save employee data to CSV and
    reports to text files.
    """
    
    @staticmethod
    def save_to_csv(employees: List[Employee], filename: str) -> None:
        """
        Save employee data to CSV file.
        
        Args:
            employees (List[Employee]): List of employees to save
            filename (str): Output CSV filename
        """
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            fieldnames = [
                'emp_id', 'name', 'department', 
                'salary', 'joining_date', 'performance_score'
            ]
            
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for emp in employees:
                writer.writerow(emp.to_dict())
        
        print(f"✅ Employee data saved to: {filename}")
    
    @staticmethod
    def save_report(report_text: str, filename: str) -> None:
        """
        Save analysis report to text file.
        
        Args:
            report_text (str): Report content to save
            filename (str): Output text filename
        """
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(report_text)
        
        print(f"✅ Analysis report saved to: {filename}")
    
    @staticmethod
    def load_from_csv(filename: str) -> List[Employee]:
        """
        Load employee data from CSV file.
        
        Args:
            filename (str): Input CSV filename
            
        Returns:
            List[Employee]: List of Employee objects loaded from file
        """
        employees = []
        
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                employee = Employee(
                    emp_id=row['emp_id'],
                    name=row['name'],
                    department=row['department'],
                    salary=float(row['salary']),
                    joining_date=row['joining_date'],
                    performance_score=float(row['performance_score'])
                )
                employees.append(employee)
        
        print(f"✅ Loaded {len(employees)} employees from: {filename}")
        return employees


def main():
    """
    Main execution function.
    
    Demonstrates the complete workflow:
    1. Generate employee data
    2. Save to CSV
    3. Analyze data
    4. Generate and save report
    """
    print("=" * 80)
    print("EMPLOYEE DATA ANALYSIS SYSTEM")
    print("=" * 80)
    print()
    
    # Step 1: Generate employee data
    print("Step 1: Generating employee data...")
    print("-" * 80)
    employees = EmployeeDataGenerator.generate_employees(100)
    print(f"✅ Generated {len(employees)} employee records")
    print()
    
    # Step 2: Save to CSV
    print("Step 2: Saving data to CSV...")
    print("-" * 80)
    FileManager.save_to_csv(employees, 'employees.csv')
    print()
    
    # Step 3: Analyze data
    print("Step 3: Analyzing employee data...")
    print("-" * 80)
    analyzer = EmployeeAnalyzer(employees)
    report = analyzer.generate_report()
    print("✅ Analysis completed")
    print()
    
    # Step 4: Save report
    print("Step 4: Saving analysis report...")
    print("-" * 80)
    FileManager.save_report(report, 'analysis_report.txt')
    print()
    
    # Step 5: Display report
    print("Step 5: Displaying analysis report...")
    print("-" * 80)
    print()
    print(report)
    
    print()
    print("=" * 80)
    print("✅ ANALYSIS COMPLETE!")
    print("=" * 80)
    print()
    print("Generated files:")
    print("  • employees.csv - Employee data")
    print("  • analysis_report.txt - Analysis report")
    print()


if __name__ == "__main__":
    main()
