import React from 'react';

const FormField = ({ field, value, onChange }) => {
  const handleChange = (e) => {
    onChange(field.name, e.target.value);
  };

  return (
    <div className="form-group">
      <label htmlFor={field.name}>{field.label}</label>
      {field.type === 'textarea' ? (
        <textarea
          id={field.name}
          name={field.name}
          value={value}
          onChange={handleChange}
          required
          rows="4"
        />
      ) : (
        <input
          type={field.type}
          id={field.name}
          name={field.name}
          value={value}
          onChange={handleChange}
          required
        />
      )}
    </div>
  );
};

export default FormField;