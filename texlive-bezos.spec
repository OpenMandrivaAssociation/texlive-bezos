# revision 25507
# category Package
# catalog-ctan /macros/latex/contrib/bezos
# catalog-date 2010-10-14 20:46:53 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-bezos
Version:	20101014
Release:	6
Summary:	Packages by Javier Bezos
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bezos
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bezos.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bezos.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of packages that provide: - tools for maths accents; - a
tool that changes page-numbering in frontmatter to arabic; -
tools for dealing with some annoyances in babel; - a tool for
making end-environment checking more meaningful; - tensorial
indexes; - support for multi-file documents; - tools for easy
entry of Spanish index entries; and - dotless i's and j's for
maths fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bezos/accents.sty
%{_texmfdistdir}/tex/latex/bezos/arabicfront.sty
%{_texmfdistdir}/tex/latex/bezos/babeltools.sty
%{_texmfdistdir}/tex/latex/bezos/checkend.sty
%{_texmfdistdir}/tex/latex/bezos/dotlessi.sty
%{_texmfdistdir}/tex/latex/bezos/esindex.sty
%{_texmfdistdir}/tex/latex/bezos/soulpos.sty
%{_texmfdistdir}/tex/latex/bezos/subdocs.sty
%{_texmfdistdir}/tex/latex/bezos/tensind.sty
%doc %{_texmfdistdir}/doc/latex/bezos/README
%doc %{_texmfdistdir}/doc/latex/bezos/accents.pdf
%doc %{_texmfdistdir}/doc/latex/bezos/accents.tex
%doc %{_texmfdistdir}/doc/latex/bezos/babeltools.pdf
%doc %{_texmfdistdir}/doc/latex/bezos/babeltools.tex
%doc %{_texmfdistdir}/doc/latex/bezos/bezos.pdf
%doc %{_texmfdistdir}/doc/latex/bezos/bezos.tex
%doc %{_texmfdistdir}/doc/latex/bezos/esindex.pdf
%doc %{_texmfdistdir}/doc/latex/bezos/esindex.tex
%doc %{_texmfdistdir}/doc/latex/bezos/soulpos.pdf
%doc %{_texmfdistdir}/doc/latex/bezos/soulpos.tex
%doc %{_texmfdistdir}/doc/latex/bezos/tensind.pdf
%doc %{_texmfdistdir}/doc/latex/bezos/tensind.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 20101014-4
+ Revision: 783481
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20101014-3
+ Revision: 782958
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20101014-2
+ Revision: 749598
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20101014-1
+ Revision: 717912
- texlive-bezos
- texlive-bezos
- texlive-bezos
- texlive-bezos
- texlive-bezos

