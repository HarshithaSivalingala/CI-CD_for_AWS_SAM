import React, { useState, useEffect } from 'react';
import { getFormStructure, submitFormData } from '../services/api';
import FormField from './FormField';

const ContactForm = () => {
  const [formStructure, setFormStructure] = useState(null);
  const [formData, setFormData] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitResult, setSubmitResult] = useState(null);

  useEffect(() => {
    const fetchFormStructure = async () => {
      try {
        const response = await getFormStructure();
        setFormStructure(response.form);
        
        // Initialize form data with empty values
        const initialData = {};
        response.form.fields.forEach(field => {
          initialData[field.name] = '';
        });
        setFormData(initialData);
      } catch (error) {
        console.error('Error loading form:', error);
      }
    };

    fetchFormStructure();
  }, []);

  const handleFieldChange = (fieldName, value) => {
    setFormData(prev => ({
      ...prev,
      [fieldName]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    setSubmitResult(null);
    
    try {
      const result = await submitFormData(formData);
      setSubmitResult({ success: true, message: result.message });
      // Reset form if submission was successful
      const resetData = {};
      Object.keys(formData).forEach(key => {
        resetData[key] = '';
      });
      setFormData(resetData);
    } catch (error) {
      setSubmitResult({ success: false, message: error.message });
    } finally {
      setIsSubmitting(false);
    }
  };

  if (!formStructure) {
    return <div>Loading form...</div>;
  }

  return (
    <div className="contact-form">
      <h1>{formStructure.title}</h1>
      
      <form onSubmit={handleSubmit}>
        {formStructure.fields.map(field => (
          <FormField
            key={field.name}
            field={field}
            value={formData[field.name] || ''}
            onChange={handleFieldChange}
          />
        ))}
        
        <button type="submit" disabled={isSubmitting}>
          {isSubmitting ? 'Submitting...' : 'Submit'}
        </button>
      </form>
      
      {submitResult && (
        <div className={`alert ${submitResult.success ? 'success' : 'error'}`}>
          {submitResult.message}
        </div>
      )}
    </div>
  );
};

export default ContactForm;