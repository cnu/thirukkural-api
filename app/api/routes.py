from flask import Blueprint, jsonify, request
from app.models.kural import KuralModel
from app.auth import token_required

api_bp = Blueprint('api', __name__)
kural_model = KuralModel()

@api_bp.route('/kurals', methods=['GET'])
@token_required
def get_all_kurals():
    """Get all Thirukkural couplets"""
    return jsonify(kural_model.get_all_kurals())

@api_bp.route('/kurals/<numbers>', methods=['GET'])
@token_required
def get_kurals(numbers):
    """
    Get one or more Thirukkural couplets by their numbers
    
    This endpoint handles both single kural requests and multiple kural requests:
    - For a single kural: /api/kurals/1
    - For multiple kurals: /api/kurals/1,2,3
    """
    kurals = kural_model.get_kurals_by_numbers(numbers)
    
    if not kurals:
        return jsonify({"error": f"No kurals found for numbers: {numbers}"}), 404
    
    # If only one kural was requested and found, still return as a list for consistency
    return jsonify(kurals)

@api_bp.route('/chapters', methods=['GET'])
@token_required
def get_all_chapters():
    """Get all chapter details"""
    return jsonify(kural_model.get_all_chapters())

@api_bp.route('/chapters/<int:chapter_number>/kurals', methods=['GET'])
@token_required
def get_kurals_by_chapter(chapter_number):
    """Get all Thirukkural couplets from a specific chapter"""
    result = kural_model.get_kurals_by_chapter(chapter_number)
    
    if 'error' in result:
        return jsonify(result), 404
    
    return jsonify(result)
