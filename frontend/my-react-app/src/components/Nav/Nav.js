import React from 'react';
import { Link } from 'react-router-dom';
import './Nav.css';

function Nav() {
  return (
    <nav>
      <ul className='navBar'>
        <li className="">
          <Link to="/">Main</Link>
        </li>
        <li className="">Main</li>
        <li className="navbarMenu">
          <Link to="/articles/">Articles</Link>
        </li>
      </ul>
    </nav>
  )
}

export default Nav;
