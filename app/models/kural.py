import json
import os
from typing import List, Dict, Any, Optional, Union

class KuralModel:
    """Model for handling Thirukkural data operations"""
    
    def __init__(self):
        self.kurals = []
        self.chapters = {}
        self._load_data()
        self._load_chapter_details()
    
    def _load_data(self) -> None:
        """Load Thirukkural data from JSON file"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_file = os.path.join(current_dir, '..', 'data', 'thirukkural.json')
        
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.kurals = data.get('kural', [])
    
    def _load_chapter_details(self) -> None:
        """Load chapter details from JSON file"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        detail_file = os.path.join(current_dir, '..', 'data', 'detail.json')
        
        with open(detail_file, 'r', encoding='utf-8') as f:
            details = json.load(f)
            
            # Process the chapter details
            for section in details[0]['section']['detail']:
                for chapter_group in section['chapterGroup']['detail']:
                    for chapter in chapter_group['chapters']['detail']:
                        chapter_num = chapter['number']
                        start = chapter['start']
                        end = chapter['end']
                        
                        self.chapters[chapter_num] = {
                            'name': chapter['name'],
                            'translation': chapter['translation'],
                            'transliteration': chapter['transliteration'],
                            'start': start,
                            'end': end,
                            'kural_numbers': list(range(start, end + 1))
                        }
    
    def get_all_kurals(self) -> List[Dict[str, Any]]:
        """Get all Thirukkural couplets"""
        return self.kurals
    
    def get_kurals_by_numbers(self, numbers: Union[str, List[int]]) -> List[Dict[str, Any]]:
        """
        Get Thirukkural couplets by their numbers
        
        Args:
            numbers: A string of comma-separated numbers or a list of integers
            
        Returns:
            List of kural dictionaries matching the specified numbers
        """
        if isinstance(numbers, str):
            # Handle comma-separated string of numbers
            try:
                # Split the string by commas and convert to integers
                number_list = [int(num.strip()) for num in numbers.split(',')]
            except ValueError:
                # If conversion fails, return empty list
                return []
        else:
            number_list = numbers
        
        # Filter kurals by the specified numbers
        return [kural for kural in self.kurals if kural['Number'] in number_list]
    
    def get_kurals_by_chapter(self, chapter_number: int) -> Dict[str, Any]:
        """
        Get all Thirukkural couplets from a specific chapter
        
        Args:
            chapter_number: The chapter number
            
        Returns:
            Dictionary with chapter details and kurals
        """
        chapter = self.chapters.get(chapter_number)
        if not chapter:
            return {'error': f'Chapter {chapter_number} not found'}
        
        chapter_kurals = [kural for kural in self.kurals 
                         if kural['Number'] >= chapter['start'] and 
                         kural['Number'] <= chapter['end']]
        
        return {
            'chapter': chapter,
            'kurals': chapter_kurals
        }
    
    def get_all_chapters(self) -> Dict[int, Dict[str, Any]]:
        """Get all chapter details"""
        return self.chapters
