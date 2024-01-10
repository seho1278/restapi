import React, { useState, useEffect } from "react";
import { useParams } from 'react-router-dom';
import axios from "axios";

import './Article.css'

function ArticleDetail() {
  const { article_pk } = useParams();
  const [article, setArticle] = useState(null);

  useEffect (() => {
    const apiUrl = `http://127.0.0.1:8000/api/v1/articles/${article_pk}`
    
    axios.get(apiUrl)
      .then(response => {
        setArticle(response.data)
      })
      .catch(error => {
        console.error('Error fetching data:', error)
      });
  }, [article_pk]);
  
  return (
    <div>
      {article && (
        <div>
          <h1>{article.title}</h1>
          <p>{article.content}</p>
        </div>
      )}
    </div>
  )
};

export default ArticleDetail;
