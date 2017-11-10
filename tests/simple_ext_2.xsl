<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:atom="http://www.w3.org/2005/Atom"
    exclude-result-prefixes="xs atom" version="2.0">

    <xsl:template match="/test">
        <pubDate>
            <xsl:apply-templates select="isodate"/>
        </pubDate>
    </xsl:template>

    <xsl:template match="isodate">
        <isodate>default impl</isodate>
    </xsl:template>


</xsl:stylesheet>
