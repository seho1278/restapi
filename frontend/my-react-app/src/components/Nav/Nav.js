import React from 'react';
import { Link } from 'react-router-dom';
import './Nav.css';

function Nav() {
  return (
    <nav className='navContainer'>
      <div className='Logo'>Logo</div>
      <ul className='navBar'>
        <li className="navbarMenu">
          <Link to="/">Main</Link>
        </li>
        <li className="navbarMenu">Main</li>
        <li className="navbarMenu">
          <Link to="/articles/">Articles</Link>
        </li>
      </ul>
      <ul className='navBar'>
        <li className='navbarMenu'>Login</li>
        <li className='navbarMenu'>Signup</li>
      </ul>
    </nav>
  )
}

export default Nav;
